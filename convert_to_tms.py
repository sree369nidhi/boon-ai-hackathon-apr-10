#!/usr/bin/env python3
"""
Convert extracted JSON files to TMS format.

This script reads extraction JSON files and converts them to the target TMS format
according to the field mapping defined in tms_field_mapping.md.
"""

import json
import os
import re
import uuid
import datetime
import argparse
from typing import Dict, List, Any, Optional, Tuple
import glob


def parse_address(address: str) -> Dict[str, str]:
    """
    Parse an address string into components (street, city, state, zip).
    
    Args:
        address: Full address string
        
    Returns:
        Dictionary with address components
    """
    if not address:
        return {"street": "", "city": "", "state": "", "zip_code": ""}
    
    # Extract zip code (assuming US format)
    zip_match = re.search(r'(\d{5}(?:-\d{4})?)', address)
    zip_code = zip_match.group(1) if zip_match else ""
    
    # Extract state (2-letter code before zip)
    state_match = re.search(r'([A-Z]{2})\s+\d{5}', address)
    state = state_match.group(1) if state_match else ""
    
    # Extract city (typically before state)
    city_match = re.search(r',\s*([^,]+?)\s+[A-Z]{2}\s+\d{5}', address)
    city = city_match.group(1) if city_match else ""
    
    # Street is everything before the city
    street_parts = address.split(',')
    street = street_parts[0] if street_parts else ""
    
    return {
        "street": street.strip(),
        "city": city.strip(),
        "state": state.strip(),
        "zip_code": zip_code.strip()
    }


def format_timestamp(timestamp_str: Optional[str]) -> str:
    """
    Format a timestamp string to TMS format (YYYYMMDDHHmmss-0700).
    
    Args:
        timestamp_str: Input timestamp string (e.g., "12/03/24 06:00")
        
    Returns:
        Formatted timestamp string or empty string if input is None
    """
    if not timestamp_str:
        return ""
    
    try:
        # Parse the input timestamp
        dt = datetime.datetime.strptime(timestamp_str, "%m/%d/%y %H:%M")
        
        # Format to TMS format with hardcoded timezone for now
        # In a production environment, we'd determine the correct timezone
        return dt.strftime("%Y%m%d%H%M%S") + "-0700"
    except ValueError:
        # If parsing fails, return empty string
        return ""


def generate_id(prefix: str = "zz") -> str:
    """
    Generate a unique ID for TMS entities.
    
    Args:
        prefix: ID prefix
        
    Returns:
        Unique ID string
    """
    # Generate a random UUID and format it
    random_part = uuid.uuid4().hex[:16]
    timestamp = datetime.datetime.now().strftime("%ifg")
    return f"{prefix}{random_part}{timestamp}APP2"


def map_equipment_type(equipment_type: str) -> str:
    """
    Map descriptive equipment type to TMS code.
    
    Args:
        equipment_type: Descriptive equipment type
        
    Returns:
        TMS equipment type code
    """
    equipment_map = {
        "Van": "V",
        "Reefer": "R",
        "Flatbed": "F",
        "Dry Van": "V",
        "Refrigerated": "R",
        "Tanker": "T",
        "Container": "C",
        "Specialized": "S"
    }
    
    return equipment_map.get(equipment_type, "V")  # Default to Van if unknown


def convert_to_tms(extraction_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert extraction JSON data to TMS format.
    
    Args:
        extraction_data: Extraction JSON data
        
    Returns:
        TMS formatted JSON data
    """
    # Initialize TMS data structure
    tms_data = {
        "__type": "orders",
        "company_id": "TMS",
        "allow_relay": True,
        "collection_method": "P",  # Prepaid
        "commodity": "DRY",
        "commodity_id": "DRY",
        "status": "A",  # Available
        "operational_status": "CLIN",
        "order_mode": "T",
        "ordered_method": "M",
        "bill_distance_um": "MI",
        "freight_charge_c": "USD",
        "total_charge_c": "USD",
        "otherchargetotal_c": "USD",
        "totalcharge_and_excisetax_c": "USD"
    }
    
    # Set reference number/bill number
    tms_data["blnum"] = extraction_data.get("reference_number", "")
    
    # Set customer ID (in production, we'd use a lookup table)
    # For now, use a simplified approach
    customer_name = extraction_data.get("customer_name", "")
    tms_data["customer_id"] = "".join([word[0] for word in customer_name.split()[:2]]).upper() if customer_name else "UNKNOWN"
    
    # Set equipment type
    equipment_type = extraction_data.get("equipment_type", "Van")
    tms_data["equipment_type_id"] = map_equipment_type(equipment_type)
    
    # Set rate information
    freight_rate = extraction_data.get("freight_rate", 0)
    total_rate = extraction_data.get("total_rate", 0)
    additional_rates = extraction_data.get("additional_rates", [])
    
    tms_data["freight_charge"] = freight_rate
    tms_data["freight_charge_n"] = freight_rate
    tms_data["freight_charge_r"] = 1
    
    tms_data["rate"] = freight_rate
    tms_data["rate_type"] = "F" if extraction_data.get("is_flat_rate", True) else "M"
    tms_data["rate_units"] = 1
    
    # Calculate other charges total
    other_charge_total = sum(rate.get("amount", 0) for rate in additional_rates)
    tms_data["otherchargetotal"] = other_charge_total
    tms_data["otherchargetotal_n"] = other_charge_total
    tms_data["otherchargetotal_r"] = 1
    
    # Set total charge
    tms_data["total_charge"] = total_rate
    tms_data["total_charge_n"] = total_rate
    tms_data["total_charge_r"] = 1
    tms_data["totalcharge_and_excisetax"] = total_rate
    tms_data["totalcharge_and_excisetax_n"] = total_rate
    tms_data["totalcharge_and_excisetax_r"] = 1
    
    # Set temperature information if present
    if extraction_data.get("temperature_present", False):
        temp_low = extraction_data.get("temperature_low")
        temp_high = extraction_data.get("temperature_high")
        
        if temp_low is not None:
            tms_data["temperature_min"] = temp_low
        
        if temp_high is not None:
            tms_data["temperature_max"] = temp_high
            
        # Calculate setpoint as average if both min and max are available
        if temp_low is not None and temp_high is not None:
            tms_data["setpoint_temp"] = (temp_low + temp_high) / 2
    
    # Set ordered date (current timestamp)
    current_time = datetime.datetime.now()
    tms_data["ordered_date"] = current_time.strftime("%Y%m%d%H%M%S-0700")
    
    # Process stops
    stops = []
    shipper_stops = extraction_data.get("shipper_section", [])
    receiver_stops = extraction_data.get("receiver_section", [])
    
    # Generate stop IDs
    shipper_stop_ids = [generate_id() for _ in shipper_stops]
    receiver_stop_ids = [generate_id() for _ in receiver_stops]
    
    # Store first and last stop IDs for the order
    if shipper_stop_ids:
        tms_data["shipper_stop_id"] = shipper_stop_ids[0]
    
    if receiver_stop_ids:
        tms_data["consignee_stop_id"] = receiver_stop_ids[-1]
    
    # Process shipper stops
    for i, shipper in enumerate(shipper_stops):
        stop_id = shipper_stop_ids[i]
        address_parts = parse_address(shipper.get("ship_from_address", ""))
        
        stop = {
            "__type": "stop",
            "company_id": "TMS",
            "id": stop_id,
            "address": address_parts["street"],
            "city_name": address_parts["city"],
            "state": address_parts["state"],
            "zip_code": address_parts["zip_code"],
            "location_name": shipper.get("ship_from_company", ""),
            "stop_type": "PU",  # Pickup
            "driver_load_unload": "N",
            "status": "A",
            "order_id": tms_data["blnum"],
            "order_sequence": i + 1,
            "movement_sequence": i + 1
        }
        
        # Set appointment times if available
        pickup_start = shipper.get("pickup_appointment_start_datetime")
        pickup_end = shipper.get("pickup_appointment_end_datetime")
        
        if pickup_start:
            stop["sched_arrive_early"] = format_timestamp(pickup_start)
            
        if pickup_end:
            stop["sched_arrive_late"] = format_timestamp(pickup_end)
        
        # Add pickup instructions as stop notes if available
        instructions = shipper.get("pickup_instructions")
        if instructions:
            stop["stopNotes"] = [{
                "__type": "stop_note",
                "company_id": "TMS",
                "comment_type": "DC",  # Dispatch comment
                "comments": instructions,
                "sequence": 1,
                "stop_id": stop_id,
                "system_added": False
            }]
            
            # Also add to loading instructions
            stop["__loadingInstructions"] = instructions
        
        # Add pickup number as reference number if available
        pickup_number = shipper.get("pickup_number")
        if pickup_number:
            stop["referenceNumbers"] = [{
                "__type": "reference_number",
                "company_id": "TMS",
                "reference_number": pickup_number,
                "reference_qual": "POL",  # Pickup number
                "send_to_driver": True,
                "stop_id": stop_id
            }]
        
        stops.append(stop)
    
    # Process receiver stops
    for i, receiver in enumerate(receiver_stops):
        stop_id = receiver_stop_ids[i]
        address_parts = parse_address(receiver.get("receiver_address", ""))
        
        stop = {
            "__type": "stop",
            "company_id": "TMS",
            "id": stop_id,
            "address": address_parts["street"],
            "city_name": address_parts["city"],
            "state": address_parts["state"],
            "zip_code": address_parts["zip_code"],
            "location_name": receiver.get("receiver_company", ""),
            "stop_type": "SO",  # Delivery
            "driver_load_unload": "N",
            "status": "A",
            "order_id": tms_data["blnum"],
            "order_sequence": len(shipper_stops) + i + 1,
            "movement_sequence": len(shipper_stops) + i + 1
        }
        
        # Set appointment times if available
        delivery_start = receiver.get("receiver_appointment_start_datetime")
        delivery_end = receiver.get("receiver_appointment_end_datetime")
        
        if delivery_start:
            stop["sched_arrive_early"] = format_timestamp(delivery_start)
            
        if delivery_end:
            stop["sched_arrive_late"] = format_timestamp(delivery_end)
        
        # Add delivery instructions as stop notes if available
        instructions = receiver.get("receiver_instructions")
        if instructions:
            stop["stopNotes"] = [{
                "__type": "stop_note",
                "company_id": "TMS",
                "comment_type": "DC",  # Dispatch comment
                "comments": instructions,
                "sequence": 1,
                "stop_id": stop_id,
                "system_added": False
            }]
            
            # Also add to unloading instructions
            stop["__unloadingInstructions"] = instructions
        
        # Add delivery number as reference number if available
        delivery_number = receiver.get("receiver_delivery_number")
        if delivery_number:
            stop["referenceNumbers"] = [{
                "__type": "reference_number",
                "company_id": "TMS",
                "reference_number": delivery_number,
                "reference_qual": "ON",  # Order number
                "send_to_driver": True,
                "stop_id": stop_id
            }]
        
        stops.append(stop)
    
    # Add stops to TMS data
    tms_data["stops"] = stops
    
    # Calculate bill distance (simplified - in production we'd use geocoding)
    # For now, use a placeholder value based on number of stops
    tms_data["bill_distance"] = (len(stops) - 1) * 100  # Placeholder
    
    # Create movement between origin and destination
    if shipper_stop_ids and receiver_stop_ids:
        # Generate a movement ID that works with any reference number format
        try:
            # Try to convert to int if it's numeric
            ref_num = ''.join(filter(str.isdigit, tms_data["blnum"]))
            if ref_num:
                movement_id = str(int(ref_num) + 1000000)
            else:
                # Fallback for completely non-numeric references
                movement_id = str(hash(tms_data["blnum"]) % 10000000 + 1000000)
        except (ValueError, TypeError):
            # Fallback for any conversion errors
            movement_id = str(hash(tms_data["blnum"]) % 10000000 + 1000000)
        
        movement = {
            "__type": "movement",
            "company_id": "TMS",
            "id": movement_id,
            "origin_stop_id": shipper_stop_ids[0],
            "dest_stop_id": receiver_stop_ids[-1],
            "loaded": "L",  # Loaded
            "movement_type": "TKLD",
            "status": "A",
            "move_distance": tms_data["bill_distance"],
            "move_distance_um": "MI",
            "authorized": True,
            "order_id": tms_data["blnum"]
        }
        
        tms_data["movement"] = [movement]
        tms_data["curr_movement_id"] = movement_id
    
    # Add other charges if present
    if additional_rates:
        other_charges = []
        for i, rate in enumerate(additional_rates):
            charge = {
                "__type": "other_charge",
                "company_id": "TMS",
                "charge_code": rate.get("code", "MISC"),
                "charge_description": rate.get("description", "Miscellaneous Charge"),
                "charge_amount": rate.get("amount", 0),
                "charge_amount_c": "USD",
                "charge_amount_n": rate.get("amount", 0),
                "charge_amount_r": 1,
                "sequence": i + 1
            }
            other_charges.append(charge)
        
        tms_data["otherCharges"] = other_charges
    
    return tms_data


def process_files(input_dir: str, output_dir: str) -> Tuple[int, List[str]]:
    """
    Process all extraction JSON files in the input directory and convert them to TMS format.
    
    Args:
        input_dir: Directory containing extraction JSON files
        output_dir: Directory to write TMS JSON files
        
    Returns:
        Tuple of (number of files processed, list of errors)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all extraction JSON files
    extraction_files = glob.glob(os.path.join(input_dir, "*_extraction.json"))
    
    processed_count = 0
    errors = []
    
    for file_path in extraction_files:
        try:
            # Extract file basename
            file_name = os.path.basename(file_path)
            reference_number = file_name.split('_')[0]
            
            # Read extraction JSON
            with open(file_path, 'r') as f:
                extraction_data = json.load(f)
            
            # Convert to TMS format
            tms_data = convert_to_tms(extraction_data)
            
            # Write TMS JSON
            output_path = os.path.join(output_dir, f"{reference_number}_tms.json")
            with open(output_path, 'w') as f:
                json.dump(tms_data, f, indent=2)
            
            processed_count += 1
            
        except Exception as e:
            errors.append(f"Error processing {file_path}: {str(e)}")
    
    return processed_count, errors


def main():
    """Main function to parse arguments and process files."""
    parser = argparse.ArgumentParser(description="Convert extraction JSON files to TMS format")
    parser.add_argument("--input", default="combined_extraction_results",
                        help="Directory containing extraction JSON files")
    parser.add_argument("--output", default="converted_tms",
                        help="Directory to write TMS JSON files")
    
    args = parser.parse_args()
    
    print(f"Converting extraction files from {args.input} to TMS format in {args.output}")
    processed_count, errors = process_files(args.input, args.output)
    
    print(f"Processed {processed_count} files")
    
    if errors:
        print(f"Encountered {len(errors)} errors:")
        for error in errors:
            print(f"  - {error}")


if __name__ == "__main__":
    main()
