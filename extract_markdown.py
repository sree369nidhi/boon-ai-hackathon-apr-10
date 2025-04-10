#!/usr/bin/env python3
"""
Markdown to Extraction JSON Converter

This script processes markdown files and extracts structured data into JSON format
using OpenAI's API. It also evaluates the accuracy of the extraction by comparing
with ground truth extraction files.
"""

import os
import json
import glob
import re
from datetime import datetime
from openai import OpenAI
import argparse
from tqdm import tqdm
import pandas as pd


# Load API key from environment or .env file
def get_api_key():
    """Get OpenAI API key from environment variable or .env file."""
    import os
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
        )

    return api_key


def load_markdown_file(file_path):
    """Load content from a markdown file."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def extract_data_with_openai(markdown_content, api_key):
    """Extract structured data from markdown content using OpenAI API."""
    client = OpenAI(api_key=api_key)

    # Define the extraction prompt
    system_prompt = """Extract the following information from the provided markdown document:
    
    - equipment_type: The type of equipment used for transport (e.g., Van, Reefer)
    - reference_number: The load/order reference number
    - booking_confirmation_number: Confirmation number for the booking (often same as reference_number)
    - total_rate: Total cost for the shipment (numeric value only)
    - freight_rate: Base freight cost (numeric value only)
    - additional_rate: Additional charges (numeric value only)
    
    - shipper_section: Array of shipper information with:
      - ship_from_company: Company name
      - ship_from_address: Full address including city, state, zip
      - pickup_number: Pickup reference number (null if not available)
      - pickup_instructions: Special instructions for pickup (null if not available)
      - pickup_appointment_start_datetime: Start time for pickup window (format: MM/DD/YY HH:MM)
      - pickup_appointment_end_datetime: End time for pickup window (format: MM/DD/YY HH:MM)
    
    - receiver_section: Array of receiver information with:
      - receiver_company: Company name
      - receiver_address: Full address including city, state, zip
      - receiver_delivery_number: Delivery reference numbers (comma-separated if multiple)
      - receiver_instructions: Special instructions for delivery (null if not available)
      - receiver_appointment_start_datetime: Start time for delivery window (format: MM/DD/YY HH:MM)
      - receiver_appointment_end_datetime: End time for delivery window (format: MM/DD/YY HH:MM)
    
    - customer_name: Name of the customer
    - email_domain: Email domain (null if not available)
    - customer_address: Customer address
    
    # Temperature-related fields (include if present in the document):
    - temperature_present: Boolean indicating if temperature control is required (true/false)
    - temperature_low: Lowest acceptable temperature (numeric value only)
    - temperature_high: Highest acceptable temperature (numeric value only)
    
    # Additional fields that may be present:
    - is_flat_rate: Boolean indicating if the rate is flat (true/false)
    - additional_rates: Array of additional charges, each with:
      - amount: The charge amount (numeric value only)
      - is_fuel_surcharge: Boolean indicating if it's a fuel surcharge (true/false)

    Format the response as a JSON object with these fields. Be precise with the data extraction.
    For dates, use the format MM/DD/YY HH:MM.
    For monetary values, extract only the numeric value without currency symbols.
    If a field is not found in the document, set it to null.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": markdown_content},
            ],
        )

        extracted_data = json.loads(response.choices[0].message.content)
        return extracted_data

    except Exception as e:
        print(f"Error during OpenAI extraction: {e}")
        return None


def post_process_extraction(extracted_data):
    """Clean up and format the extracted data."""
    if not extracted_data:
        return {}

    # Format monetary values to ensure they're numeric
    for field in ["total_rate", "freight_rate", "additional_rate"]:
        if field in extracted_data and extracted_data[field]:
            # Remove any non-numeric characters except decimal point
            if isinstance(extracted_data[field], str):
                extracted_data[field] = re.sub(r"[^\d.]", "", extracted_data[field])

            # Convert to float
            try:
                extracted_data[field] = float(extracted_data[field])
            except (ValueError, TypeError):
                extracted_data[field] = None

    # Process temperature values
    for field in ["temperature_low", "temperature_high"]:
        if field in extracted_data and extracted_data[field]:
            # Remove any non-numeric characters except decimal point
            if isinstance(extracted_data[field], str):
                extracted_data[field] = re.sub(r"[^\d.-]", "", extracted_data[field])

            # Convert to float
            try:
                extracted_data[field] = float(extracted_data[field])
            except (ValueError, TypeError):
                extracted_data[field] = None

    # Process additional_rates if present
    if "additional_rates" in extracted_data and extracted_data["additional_rates"]:
        for rate in extracted_data["additional_rates"]:
            if "amount" in rate and rate["amount"]:
                # Remove any non-numeric characters except decimal point
                if isinstance(rate["amount"], str):
                    rate["amount"] = re.sub(r"[^\d.]", "", rate["amount"])

                # Convert to float
                try:
                    rate["amount"] = float(rate["amount"])
                except (ValueError, TypeError):
                    rate["amount"] = None

    # Process shipper section
    if "shipper_section" in extracted_data and extracted_data["shipper_section"]:
        for shipper in extracted_data["shipper_section"]:
            # Format dates
            for date_field in [
                "pickup_appointment_start_datetime",
                "pickup_appointment_end_datetime",
            ]:
                if date_field in shipper and shipper[date_field]:
                    shipper[date_field] = format_date(shipper[date_field])

    # Process receiver section
    if "receiver_section" in extracted_data and extracted_data["receiver_section"]:
        for receiver in extracted_data["receiver_section"]:
            # Format dates
            for date_field in [
                "receiver_appointment_start_datetime",
                "receiver_appointment_end_datetime",
            ]:
                if date_field in receiver and receiver[date_field]:
                    receiver[date_field] = format_date(receiver[date_field])

    # Ensure boolean fields are properly formatted
    for field in ["temperature_present", "is_flat_rate"]:
        if field in extracted_data:
            if isinstance(extracted_data[field], str):
                extracted_data[field] = extracted_data[field].lower() == "true"

    return extracted_data


def format_date(date_str):
    """Format date string to MM/DD/YY HH:MM format."""
    if not date_str:
        return None

    # Try different date formats
    date_formats = [
        "%m/%d/%y %H:%M",
        "%m/%d/%Y %H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%m/%d/%y",
        "%m/%d/%Y",
        "%Y-%m-%d",
    ]

    # Extract date and time components
    date_match = re.search(r"(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", date_str)
    time_match = re.search(r"(\d{1,2}:\d{2})", date_str)

    if date_match:
        date_part = date_match.group(1)
        time_part = time_match.group(1) if time_match else "00:00"

        # Replace slashes with standard format
        date_part = date_part.replace("-", "/")

        # Try to parse the date
        for fmt in date_formats:
            try:
                date_obj = datetime.strptime(f"{date_part} {time_part}", fmt)
                return date_obj.strftime("%m/%d/%y %H:%M")
            except ValueError:
                continue

    # If we can't parse it, return as is
    return date_str


def get_all_fields(json_obj, prefix=""):
    """Get all fields in a JSON object recursively."""
    fields = set()

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            field_name = f"{prefix}.{key}" if prefix else key
            fields.add(field_name)

            if isinstance(value, (dict, list)):
                fields.update(get_all_fields(value, field_name))

    elif isinstance(json_obj, list):
        for i, item in enumerate(json_obj):
            field_name = f"{prefix}[{i}]"
            fields.update(get_all_fields(item, field_name))

    return fields


def get_field_value(json_obj, field_path):
    """Get value of a field specified by its path."""
    parts = field_path.split(".")
    current = json_obj

    for part in parts:
        # Handle array indexing
        if "[" in part and "]" in part:
            array_name, idx_str = part.split("[", 1)
            idx = int(idx_str.rstrip("]"))

            if (
                array_name in current
                and isinstance(current[array_name], list)
                and idx < len(current[array_name])
            ):
                current = current[array_name][idx]
            else:
                return None
        else:
            if part in current:
                current = current[part]
            else:
                return None

    return current


def calculate_accuracy(extracted_json, ground_truth_json):
    """Calculate accuracy metrics by comparing extracted data with ground truth."""
    metrics = {
        "field_presence": 0,  # Percentage of expected fields present
        "field_accuracy": 0,  # Percentage of fields with correct values
        "overall_accuracy": 0,  # Weighted combination of above metrics
    }

    # Get all fields from ground truth
    ground_truth_fields = get_all_fields(ground_truth_json)

    # Calculate field presence
    present_fields = 0
    for field in ground_truth_fields:
        extracted_value = get_field_value(extracted_json, field)
        if extracted_value is not None:
            present_fields += 1

    metrics["field_presence"] = (
        present_fields / len(ground_truth_fields) if ground_truth_fields else 0
    )

    # Calculate field accuracy
    correct_fields = 0
    for field in ground_truth_fields:
        ground_truth_value = get_field_value(ground_truth_json, field)
        extracted_value = get_field_value(extracted_json, field)

        # Skip if field is not present in extraction
        if extracted_value is None:
            continue

        # Compare values (with type conversion for numeric fields)
        if isinstance(ground_truth_value, (int, float)) and isinstance(
            extracted_value, (int, float)
        ):
            # Allow small differences for numeric values
            if abs(ground_truth_value - extracted_value) < 0.01:
                correct_fields += 1
        elif str(ground_truth_value).lower() == str(extracted_value).lower():
            correct_fields += 1

    metrics["field_accuracy"] = (
        correct_fields / len(ground_truth_fields) if ground_truth_fields else 0
    )

    # Calculate overall accuracy (weighted)
    metrics["overall_accuracy"] = (
        0.4 * metrics["field_presence"] + 0.6 * metrics["field_accuracy"]
    )

    return metrics


def generate_accuracy_report(results, output_file):
    """Generate a report of accuracy metrics."""
    df = pd.DataFrame(results)

    # Calculate average metrics
    avg_metrics = {
        "field_presence": df["accuracy"].apply(lambda x: x["field_presence"]).mean(),
        "field_accuracy": df["accuracy"].apply(lambda x: x["field_accuracy"]).mean(),
        "overall_accuracy": df["accuracy"]
        .apply(lambda x: x["overall_accuracy"])
        .mean(),
    }

    # Save detailed results
    df.to_csv(output_file, index=False)

    # Print summary
    print("\nAccuracy Report:")
    print(f"Average Field Presence: {avg_metrics['field_presence']:.2%}")
    print(f"Average Field Accuracy: {avg_metrics['field_accuracy']:.2%}")
    print(f"Average Overall Accuracy: {avg_metrics['overall_accuracy']:.2%}")
    print(f"Detailed results saved to {output_file}")

    return avg_metrics


def main():
    parser = argparse.ArgumentParser(
        description="Extract structured data from markdown files using OpenAI API"
    )
    parser.add_argument(
        "--markdown-dir",
        default="hackathon_dataset_organized/markdown",
        help="Directory containing markdown files",
    )
    parser.add_argument(
        "--extraction-dir",
        default="hackathon_dataset_organized/extraction",
        help="Directory containing ground truth extraction files",
    )
    parser.add_argument(
        "--output-dir",
        default="our_extraction_results",
        help="Directory to save extraction results",
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=0,
        help="Process only a sample of files (0 for all files)",
    )
    args = parser.parse_args()

    # 1. Set up paths
    markdown_dir = args.markdown_dir
    extraction_dir = args.extraction_dir
    output_dir = args.output_dir

    # 2. Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # 3. Get API key
    api_key = get_api_key()

    # 4. Process each markdown file
    markdown_files = glob.glob(os.path.join(markdown_dir, "*.md"))

    # Limit to sample size if specified
    if args.sample > 0:
        markdown_files = markdown_files[: args.sample]

    results = []
    for md_file in tqdm(markdown_files, desc="Processing files"):
        # Extract file ID
        file_id = os.path.basename(md_file).split(".")[0]

        # Load markdown content
        markdown_content = load_markdown_file(md_file)

        # Extract data using OpenAI
        extracted_data = extract_data_with_openai(markdown_content, api_key)

        # Post-process the extracted data
        processed_data = post_process_extraction(extracted_data)

        # Save the extraction result
        output_file = os.path.join(output_dir, f"{file_id}_extraction.json")
        with open(output_file, "w") as f:
            json.dump(processed_data, f, indent=2)

        # Calculate accuracy if ground truth exists
        ground_truth_file = os.path.join(extraction_dir, f"{file_id}_extraction.json")
        if os.path.exists(ground_truth_file):
            with open(ground_truth_file, "r") as f:
                ground_truth = json.load(f)

            accuracy = calculate_accuracy(processed_data, ground_truth)
            results.append({"file_id": file_id, "accuracy": accuracy})

    # 5. Generate accuracy report
    if results:
        report_file = os.path.join(output_dir, "accuracy_report.csv")
        generate_accuracy_report(results, report_file)


if __name__ == "__main__":
    main()
