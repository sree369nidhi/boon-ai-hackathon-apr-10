#!/usr/bin/env python3
"""
Parallel LLM-based TMS Conversion

This script converts extraction JSON files to TMS format using OpenAI's API
with parallel processing to speed up the conversion.
"""

import json
import os
import re
import uuid
import datetime
import argparse
import glob
import time
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm
from difflib import SequenceMatcher
import concurrent.futures
import threading

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load customer ID mapping
CUSTOMER_ID_MAPPING = {}
try:
    with open('customer_id_mapping.json', 'r') as f:
        CUSTOMER_ID_MAPPING = json.load(f)
    print(f"Loaded {len(CUSTOMER_ID_MAPPING)} customer ID mappings")
except FileNotFoundError:
    print("Warning: customer_id_mapping.json not found. Will rely on LLM for customer ID mapping.")

# Thread-local storage for OpenAI clients
thread_local = threading.local()

# TMS template with examples for the LLM to learn from
TMS_TEMPLATE = """
You are tasked with converting extraction JSON data to TMS (Transportation Management System) format.
Follow these guidelines to ensure accurate conversion:

1. The TMS format has a specific structure with fields like company_id, customer_id, blnum, etc.
2. Ensure all dates are in the format "YYYYMMDDHHMMSS-0700" (or appropriate timezone).
3. Generate appropriate IDs for stops and movements using the format provided below.
4. Map customer names to customer_ids correctly using the suggested customer_id if provided.
5. Properly format addresses and contact information.
6. Calculate distances between stops accurately.
7. Set appropriate status codes (e.g., "A" for Available).
8. Include all required fields shown in the template below.

Here's the expected TMS structure:
```json
{
  "__type": "orders",
  "company_id": "TMS",
  "allow_relay": true,
  "autorate_status": "",
  "bill_date": "",
  "bill_distance": [DISTANCE_IN_MILES],
  "bill_distance_um": "MI",
  "billing_user_id": "",
  "blnum": "[ORDER_NUMBER]",
  "bol_received": false,
  "bol_recv_date": "",
  "collection_method": "P",
  "commodity": "DRY",
  "commodity_id": "DRY",
  "consignee_refno": "",
  "consignee_stop_id": "[GENERATED_DELIVERY_STOP_ID]",
  "curr_movement_id": "[GENERATED_MOVEMENT_ID]",
  "customer_id": "[CUSTOMER_ID]",
  "def_move_type": "A",
  "dispatch_opt": true,
  "entered_user_id": "boonai",
  "est_tolls": 0,
  "est_tolls_c": "USD",
  "est_tolls_d": "[CURRENT_TIMESTAMP]",
  "est_tolls_n": 0,
  "est_tolls_r": 1,
  "excise_disable_update": false,
  "excise_taxable": false,
  "excisetax_total": 0,
  "excisetax_total_c": "USD",
  "excisetax_total_d": "[CURRENT_TIMESTAMP]",
  "excisetax_total_n": 0,
  "excisetax_total_r": 1,
  "extra_deliveries": 0,
  "extra_pickups": 0,
  "force_assign": true,
  "freight_charge": [FREIGHT_AMOUNT],
  "freight_charge_c": "USD",
  "freight_charge_d": "[CURRENT_TIMESTAMP]",
  "freight_charge_n": [FREIGHT_AMOUNT],
  "freight_charge_r": 1,
  "hazmat": false,
  "high_value": false,
  "id": "[GENERATED_ORDER_ID]",
  "include_split_point": false,
  "is_autorate_dist": false,
  "is_container": false,
  "is_dedicated": false,
  "is_local_mile": false,
  "loadboard": false,
  "ltl": false,
  "next_rebill": "",
  "on_hold": false,
  "operational_status": "CLIN",
  "operations_user": "boonai",
  "order_mode": "T",
  "ordered_date": "[CURRENT_TIMESTAMP]",
  "ordered_method": "M",
  "otherchargetotal": 0,
  "otherchargetotal_c": "USD",
  "otherchargetotal_d": "[CURRENT_TIMESTAMP]",
  "otherchargetotal_n": 0,
  "otherchargetotal_r": 1,
  "pallets_required": false,
  "pay_gross": 0,
  "pay_gross_c": "",
  "pay_gross_d": "",
  "pay_gross_n": 0,
  "pay_gross_r": 0,
  "pieces": 0,
  "pnn_post_type": "",
  "preloaded": false,
  "rate": [FREIGHT_AMOUNT],
  "rate_min_weight": 0,
  "rate_type": "F",
  "rate_units": 1,
  "ready_to_bill": false,
  "recurring_order_id": null,
  "reply_transmitted": false,
  "revenue_code_id": "GEN",
  "round_trip": false,
  "ship_status_to_edi": false,
  "shipper_stop_id": "[GENERATED_PICKUP_STOP_ID]",
  "shipstatus2edi_dt": "",
  "status": "A",
  "swap": true,
  "teams_required": false,
  "total_charge": [FREIGHT_AMOUNT],
  "total_charge_c": "USD",
  "total_charge_d": "[CURRENT_TIMESTAMP]",
  "total_charge_n": [FREIGHT_AMOUNT],
  "total_charge_r": 1,
  "totalcharge_and_excisetax": [FREIGHT_AMOUNT],
  "totalcharge_and_excisetax_c": "USD",
  "totalcharge_and_excisetax_d": "[CURRENT_TIMESTAMP]",
  "totalcharge_and_excisetax_n": [FREIGHT_AMOUNT],
  "totalcharge_and_excisetax_r": 1,
  "weight": 0,
  "weight_um": "LB",
  "xferred2billing": false,
  "xferred2billing_dt": "",
  "lock_miles": false,
  "__statusDescr": "Available",
  "__collectionMethodDescr": "Prepaid",
  "__rateTypeDescr": "Flat",
  "__revenueTypeDescr": "GENERAL FREIGHT",
  "equipment_type_id": "V",
  "billing_loaded_distance": [DISTANCE_IN_MILES],
  "billing_empty_distance": 0,
  "__equipmentTypeDescr": "Van (DAT)",
  "stops": [
    {
      "__type": "stop",
      "company_id": "TMS",
      "actual_arrival": "",
      "actual_departure": "",
      "address": "[PICKUP_ADDRESS]",
      "address2": null,
      "appt_required": false,
      "city_name": "[PICKUP_CITY]",
      "confirmed": false,
      "contact_name": "[PICKUP_CONTACT]",
      "driver_load_unload": "N",
      "id": "[GENERATED_PICKUP_STOP_ID]",
      "late_eta_colorcode": false,
      "latitude": [PICKUP_LAT],
      "location_id": "[LOCATION_ID]",
      "location_name": "[PICKUP_LOCATION_NAME]",
      "longitude": [PICKUP_LONG],
      "manifest_fgp_uid": [GENERATED_FGP_UID],
      "movement_id": "[GENERATED_MOVEMENT_ID]",
      "movement_sequence": 1,
      "order_id": "[GENERATED_ORDER_ID]",
      "order_sequence": 1,
      "phone": "[PICKUP_PHONE]",
      "prior_uncleared_stops": false,
      "requested_service": false,
      "sched_arrive_early": "[PICKUP_DATE_TIME]",
      "sched_arrive_late": "[PICKUP_DATE_TIME_PLUS_WINDOW]",
      "state": "[PICKUP_STATE]",
      "status": "A",
      "stop_type": "PU",
      "txl_uid": [GENERATED_TXL_UID],
      "zip_code": "[PICKUP_ZIP]",
      "zone_id": "[ZONE_ID]",
      "__statusDescr": "Available",
      "__typeDescr": "Pickup",
      "__loadUnloadDescr": "No driver loading or unload",
      "cases": 0,
      "weight": 0,
      "referenceNumbers": [
        {
          "__type": "reference_number",
          "company_id": "TMS",
          "element_id": "128",
          "id": "[GENERATED_REF_ID]",
          "partner_id": "TMS",
          "reference_number": "[PICKUP_REFERENCE_NUMBER]",
          "reference_qual": "PU",
          "send_to_driver": true,
          "stop_id": "[GENERATED_PICKUP_STOP_ID]",
          "version": "004010",
          "__referenceQualDescr": "Pickup Number",
          "description": "Pickup Number"
        }
      ]
    },
    {
      "__type": "stop",
      "company_id": "TMS",
      "actual_arrival": "",
      "actual_departure": "",
      "address": "[DELIVERY_ADDRESS]",
      "address2": null,
      "appt_required": false,
      "city_name": "[DELIVERY_CITY]",
      "confirmed": false,
      "contact_name": "[DELIVERY_CONTACT]",
      "driver_load_unload": "N",
      "id": "[GENERATED_DELIVERY_STOP_ID]",
      "late_eta_colorcode": false,
      "latitude": [DELIVERY_LAT],
      "location_id": "[LOCATION_ID]",
      "location_name": "[DELIVERY_LOCATION_NAME]",
      "longitude": [DELIVERY_LONG],
      "manifest_fgp_uid": [GENERATED_FGP_UID],
      "move_dist_from_previous": [DISTANCE_IN_MILES],
      "move_dist_from_previous_um": "MI",
      "movement_id": "[GENERATED_MOVEMENT_ID]",
      "movement_sequence": 2,
      "order_id": "[GENERATED_ORDER_ID]",
      "order_sequence": 2,
      "phone": "[DELIVERY_PHONE]",
      "prior_uncleared_stops": false,
      "requested_service": false,
      "sched_arrive_early": "[DELIVERY_DATE_TIME]",
      "sched_arrive_late": "[DELIVERY_DATE_TIME_PLUS_WINDOW]",
      "state": "[DELIVERY_STATE]",
      "status": "A",
      "stop_type": "SO",
      "txl_uid": [GENERATED_TXL_UID_2],
      "zip_code": "[DELIVERY_ZIP]",
      "zone_id": "[ZONE_ID]",
      "__statusDescr": "Available",
      "__typeDescr": "Delivery",
      "__loadUnloadDescr": "No driver loading or unload",
      "cases": 0,
      "weight": 0,
      "rate_dist_from_previous": [DISTANCE_IN_MILES],
      "rate_dist_from_previous_um": "MI",
      "referenceNumbers": [
        {
          "__type": "reference_number",
          "company_id": "TMS",
          "element_id": "128",
          "id": "[GENERATED_REF_ID_2]",
          "partner_id": "TMS",
          "reference_number": "[DELIVERY_REFERENCE_NUMBER]",
          "reference_qual": "ON",
          "send_to_driver": true,
          "stop_id": "[GENERATED_DELIVERY_STOP_ID]",
          "version": "004010",
          "__referenceQualDescr": "Dealer Order Number",
          "description": "Dealer Order Number"
        }
      ]
    }
  ],
  "movement": [
    {
      "__type": "movement",
      "company_id": "TMS",
      "authorized": true,
      "brokerage": false,
      "dest_stop_id": "[GENERATED_DELIVERY_STOP_ID]",
      "dispatcher_user_id": "",
      "eform_rate_confirmation": false,
      "equipment_group_id": "[EQUIPMENT_GROUP_ID]",
      "est_tolls": 0,
      "est_tolls_c": "USD",
      "est_tolls_d": "[CURRENT_TIMESTAMP]",
      "est_tolls_n": 0,
      "est_tolls_r": 1,
      "exclude_movement": false,
      "freight_matching_override": false,
      "fuel_distance": [DISTANCE_IN_MILES],
      "fuel_distance_um": "MI",
      "id": "[GENERATED_MOVEMENT_ID]",
      "integrated_carrier_search": false,
      "is_container": false,
      "is_dray": false,
      "is_local_mile": false,
      "loaded": "L",
      "ltl": false,
      "missed_call_sent": false,
      "move_distance": [DISTANCE_IN_MILES],
      "move_distance_um": "MI",
      "movement_type": "TKLD",
      "operations_user": "boonai",
      "origin_stop_id": "[GENERATED_PICKUP_STOP_ID]",
      "preassign_sequence": 1,
      "priority": false,
      "reminder_sent": false,
      "require_tracking": false,
      "reserved": false,
      "status": "A",
      "triumphpay_exclude": false,
      "trp_uid": [GENERATED_TRP_UID],
      "waterfall_in_progress": false,
      "xfer2settle_date": "",
      "is_intercompany": false,
      "order_id": "[GENERATED_ORDER_ID]",
      "empty2next_order": null
    }
  ],
  "freightGroup": {
    "__type": "freight_group",
    "company_id": "TMS",
    "add_timestamp": "[CURRENT_TIMESTAMP]",
    "add_userid": "loadmaster",
    "bol_processed": false,
    "cons_plc_uid": 0,
    "conveyance_owner_plc_uid": 0,
    "dest_txl_uid": [GENERATED_TXL_UID_2],
    "fgp_status_code": "4",
    "fgp_type_code": "DFLT",
    "fgp_uid": [GENERATED_FGP_UID],
    "lme_order_id": "[GENERATED_ORDER_ID]",
    "mod_timestamp": "[CURRENT_TIMESTAMP]",
    "mod_userid": "loadmaster",
    "ord_uid": 0,
    "orig_txl_uid": [GENERATED_TXL_UID],
    "ship_plc_uid": 0,
    "weight_uom_type_code": "LBS",
    "exceeds_volume": null,
    "fgpXBfgs": [
      {
        "__type": "fgp_x_bfg",
        "company_id": "TMS",
        "bfg_uid": [GENERATED_BFG_UID],
        "fgp_uid": [GENERATED_FGP_UID],
        "fxb_uid": [GENERATED_FXB_UID],
        "add_userid": null,
        "add_timestamp": null
      }
    ]
  }
}
```

Please convert the provided extraction data to this TMS format, ensuring all required fields are populated correctly. For any fields where information is not available in the extraction data, use reasonable defaults or generate appropriate values.
"""

def similar(a: str, b: str) -> float:
    """
    Calculate similarity ratio between two strings.
    
    Args:
        a: First string
        b: Second string
        
    Returns:
        Similarity ratio (0.0 to 1.0)
    """
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    
    return SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio()


def get_customer_id(customer_name: str) -> str:
    """
    Get customer ID from customer name using the mapping file or fuzzy matching.
    
    Args:
        customer_name: Customer name
        
    Returns:
        Customer ID
    """
    if not customer_name:
        return "UNKNOWN"
    
    # Check for exact match
    if customer_name in CUSTOMER_ID_MAPPING:
        return CUSTOMER_ID_MAPPING[customer_name]
    
    # Try fuzzy matching
    best_match = None
    best_score = 0.0
    
    for name, customer_id in CUSTOMER_ID_MAPPING.items():
        score = similar(customer_name, name)
        if score > best_score and score > 0.8:  # 80% similarity threshold
            best_score = score
            best_match = customer_id
    
    if best_match:
        return best_match
    
    # If no match found, generate a simple ID (first letters of words)
    return ''.join([word[0] for word in customer_name.split()[:2]]).upper() if customer_name else "UNKNOWN"


def get_thread_client():
    """
    Get a thread-local OpenAI client.
    """
    if not hasattr(thread_local, "client"):
        thread_local.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return thread_local.client


def convert_with_llm(extraction_data: dict) -> dict:
    """
    Convert extraction JSON data to TMS format using OpenAI's API.
    
    Args:
        extraction_data: Extraction JSON data
        
    Returns:
        TMS formatted JSON data
    """
    # Get thread-local client
    client = get_thread_client()
    
    # Try to get customer ID from mapping
    customer_name = extraction_data.get("customer_name", "")
    customer_id = get_customer_id(customer_name)
    
    # Prepare the prompt with the extraction data and customer ID
    prompt = f"{TMS_TEMPLATE}\nExtraction data:\n{json.dumps(extraction_data, indent=2)}\n\nSuggested customer_id for '{customer_name}': {customer_id}"
    
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that converts extraction data to TMS format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            max_tokens=4000
        )
        
        # Extract the response
        tms_json_str = response.choices[0].message.content
        
        # Log the mapping for future reference
        if customer_name and customer_name not in CUSTOMER_ID_MAPPING:
            try:
                # Try to extract customer ID from the response
                match = re.search(r'"customer_id"\s*:\s*"([^"]+)"', tms_json_str)
                if match:
                    extracted_id = match.group(1)
                    print(f"New mapping: '{customer_name}' -> '{extracted_id}'")
                    # Could save this to the mapping file for future use
            except Exception:
                pass
        
        # Extract JSON from the response (in case there's additional text)
        json_match = re.search(r'```json\n(.*?)\n```', tms_json_str, re.DOTALL)
        if json_match:
            tms_json_str = json_match.group(1)
        else:
            # If no code block, try to find JSON directly
            json_match = re.search(r'({.*})', tms_json_str, re.DOTALL)
            if json_match:
                tms_json_str = json_match.group(1)
        
        # Parse the JSON
        try:
            tms_data = json.loads(tms_json_str)
        except json.JSONDecodeError:
            # If parsing fails, apply post-processing to fix common issues
            tms_json_str = tms_json_str.replace("'", '"')
            tms_json_str = re.sub(r',\s*}', '}', tms_json_str)
            try:
                tms_data = json.loads(tms_json_str)
            except json.JSONDecodeError:
                # If still fails, return a basic structure with error info
                return {
                    "__type": "orders",
                    "company_id": "TMS",
                    "error": "Failed to parse LLM response",
                    "blnum": extraction_data.get("reference_number", ""),
                    "customer_id": "UNKNOWN"
                }
        
        # Ensure required fields are present
        if "stops" not in tms_data and (extraction_data.get("shipper_section") or extraction_data.get("receiver_section")):
            # Create stops array if missing
            tms_data["stops"] = []
            
            # Add shipper stop if available
            if extraction_data.get("shipper_section"):
                shipper = extraction_data["shipper_section"][0]
                tms_data["stops"].append({
                    "__type": "stop",
                    "company_id": "TMS",
                    "address": shipper.get("ship_from_address", ""),
                    "stop_type": "PU",
                    "order_sequence": 1
                })
            
            # Add receiver stop if available
            if extraction_data.get("receiver_section"):
                receiver = extraction_data["receiver_section"][0]
                tms_data["stops"].append({
                    "__type": "stop",
                    "company_id": "TMS",
                    "address": receiver.get("receiver_address", ""),
                    "stop_type": "SO",
                    "order_sequence": 2
                })
        
        return tms_data
    
    except Exception as e:
        print(f"Error converting file: {e}")
        return {
            "__type": "orders",
            "company_id": "TMS",
            "error": str(e),
            "blnum": extraction_data.get("reference_number", ""),
            "customer_id": "UNKNOWN"
        }


def process_file(extraction_file: str, output_dir: str) -> bool:
    """
    Process a single extraction file and convert it to TMS format.
    
    Args:
        extraction_file: Path to extraction JSON file
        output_dir: Directory to save TMS file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Load extraction data
        with open(extraction_file, 'r') as f:
            extraction_data = json.load(f)
        
        # Convert to TMS format
        tms_data = convert_with_llm(extraction_data)
        
        # Generate output file path
        file_id = os.path.basename(extraction_file).replace('_extraction.json', '')
        output_file = os.path.join(output_dir, f"{file_id}_tms.json")
        
        # Save TMS data
        with open(output_file, 'w') as f:
            json.dump(tms_data, f, indent=2)
        
        return True
    
    except Exception as e:
        print(f"Error processing {extraction_file}: {e}")
        return False


def main():
    """Main function to parse arguments and convert extraction files to TMS format."""
    parser = argparse.ArgumentParser(description="Convert extraction JSON files to TMS format using OpenAI API")
    parser.add_argument("--input-dir", default="combined_extraction_results",
                        help="Directory containing extraction JSON files")
    parser.add_argument("--output-dir", default="llm_converted_tms",
                        help="Directory to save TMS files")
    parser.add_argument("--sample", type=int, default=0,
                        help="Process only a sample of files (0 for all files)")
    parser.add_argument("--workers", type=int, default=5,
                        help="Number of parallel workers")
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Find all extraction files
    extraction_files = glob.glob(os.path.join(args.input_dir, "**", "*_extraction.json"), recursive=True)
    
    # Limit to sample size if specified
    if args.sample > 0:
        extraction_files = extraction_files[:args.sample]
    
    print(f"Converting extraction files from {args.input_dir} to TMS format in {args.output_dir}")
    
    # Process files in parallel
    success_count = 0
    error_files = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        # Submit all tasks
        future_to_file = {
            executor.submit(process_file, file, args.output_dir): file
            for file in extraction_files
        }
        
        # Process results as they complete
        for future in tqdm(concurrent.futures.as_completed(future_to_file), 
                          total=len(extraction_files), 
                          desc="Converting files"):
            file = future_to_file[future]
            try:
                if future.result():
                    success_count += 1
                else:
                    error_files.append(file)
            except Exception as e:
                print(f"Error processing {file}: {e}")
                error_files.append(file)
    
    print(f"Processed {success_count} files")
    
    if error_files:
        print(f"Encountered {len(error_files)} errors:")
        for file in error_files[:10]:  # Show first 10 errors
            print(f"  - Error processing {file}")
        if len(error_files) > 10:
            print(f"  ... and {len(error_files) - 10} more")


if __name__ == "__main__":
    main()
