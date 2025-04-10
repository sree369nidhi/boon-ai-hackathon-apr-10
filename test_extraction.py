#!/usr/bin/env python3
"""
Test Extraction Script

This script tests the extraction pipeline on a small sample of markdown files
to verify that everything is working correctly before running on the full dataset.
"""

import os
import json
import random
import argparse
from extract_markdown import load_markdown_file, extract_data_with_openai, post_process_extraction, get_api_key

def main():
    parser = argparse.ArgumentParser(description='Test extraction pipeline on a small sample')
    parser.add_argument('--markdown-dir', default='hackathon_dataset_organized/markdown', 
                        help='Directory containing markdown files')
    parser.add_argument('--output-dir', default='test_extraction_results', 
                        help='Directory to save test extraction results')
    parser.add_argument('--sample-size', type=int, default=2, 
                        help='Number of files to sample for testing')
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Get list of markdown files
    markdown_files = [f for f in os.listdir(args.markdown_dir) if f.endswith('.md')]
    
    # Randomly sample files
    if args.sample_size > len(markdown_files):
        print(f"Warning: Sample size ({args.sample_size}) is larger than available files ({len(markdown_files)})")
        sample_files = markdown_files
    else:
        sample_files = random.sample(markdown_files, args.sample_size)
    
    print(f"Testing extraction on {len(sample_files)} files...")
    
    # Get API key
    api_key = get_api_key()
    
    # Process each sampled file
    for md_file in sample_files:
        file_id = os.path.basename(md_file).split('.')[0]
        print(f"\nProcessing {file_id}...")
        
        # Load markdown content
        file_path = os.path.join(args.markdown_dir, md_file)
        markdown_content = load_markdown_file(file_path)
        
        # Extract data using OpenAI
        print("Extracting data with OpenAI...")
        extracted_data = extract_data_with_openai(markdown_content, api_key)
        
        if not extracted_data:
            print(f"Error: Failed to extract data from {file_id}")
            continue
        
        # Post-process the extracted data
        print("Post-processing extracted data...")
        processed_data = post_process_extraction(extracted_data)
        
        # Save the extraction result
        output_file = os.path.join(args.output_dir, f"{file_id}_extraction.json")
        with open(output_file, 'w') as f:
            json.dump(processed_data, f, indent=2)
        
        print(f"Extraction result saved to {output_file}")
        
        # Display a sample of the extracted data
        print("\nExtracted data sample:")
        print(f"Equipment Type: {processed_data.get('equipment_type', 'N/A')}")
        print(f"Reference Number: {processed_data.get('reference_number', 'N/A')}")
        print(f"Total Rate: {processed_data.get('total_rate', 'N/A')}")
        
        # Display temperature information if present
        if processed_data.get('temperature_present'):
            print("\nTemperature Information:")
            print(f"Temperature Present: {processed_data.get('temperature_present')}")
            print(f"Temperature Low: {processed_data.get('temperature_low', 'N/A')}")
            print(f"Temperature High: {processed_data.get('temperature_high', 'N/A')}")
        
        # Display additional rates if present
        if processed_data.get('additional_rates'):
            print("\nAdditional Rates:")
            for i, rate in enumerate(processed_data['additional_rates']):
                print(f"  Rate {i+1}: {rate.get('amount', 'N/A')} (Fuel Surcharge: {rate.get('is_fuel_surcharge', 'N/A')})")
        
        if 'shipper_section' in processed_data and processed_data['shipper_section']:
            shipper = processed_data['shipper_section'][0]
            print(f"\nShipper: {shipper.get('ship_from_company', 'N/A')}")
            print(f"Pickup Instructions: {shipper.get('pickup_instructions', 'N/A')}")
        
        if 'receiver_section' in processed_data and processed_data['receiver_section']:
            receiver = processed_data['receiver_section'][0]
            print(f"\nReceiver: {receiver.get('receiver_company', 'N/A')}")
            print(f"Delivery Instructions: {receiver.get('receiver_instructions', 'N/A')}")
    
    print("\nTest extraction completed!")
    print(f"Results saved to {args.output_dir}")

if __name__ == "__main__":
    main()
