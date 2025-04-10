# Part 1 Plan: Markdown to Extraction JSON Conversion

## Overview

The first part of the hackathon challenge involves converting markdown files to extraction JSON files. These extraction files will later be mapped to TMS JSON format in Part 2. This document outlines the plan for Part 1.

## Task Breakdown

1. **Data Understanding**
   - Analyze the structure of markdown files
   - Identify the expected fields in the extraction JSON
   - Understand the relationship between markdown content and extraction JSON fields

2. **Extraction Pipeline Development**
   - Create a Python script to process markdown files
   - Use OpenAI API to extract structured data from markdown
   - Format the extracted data into the expected JSON structure

3. **Accuracy Evaluation**
   - Define metrics to compare our extraction results with provided extraction files
   - Implement evaluation logic to calculate accuracy scores
   - Analyze error patterns to improve extraction quality

## Expected Extraction JSON Structure

Based on the sample extraction JSON files, we need to extract the following key fields:

- `equipment_type`: Type of equipment (e.g., "Van")
- `reference_number`: The load/order reference number
- `booking_confirmation_number`: Confirmation number for the booking
- `total_rate`: Total cost for the shipment
- `freight_rate`: Base freight cost
- `additional_rate`: Additional charges
- `shipper_section`: Array of shipper information
  - `ship_from_company`: Company name
  - `ship_from_address`: Full address
  - `pickup_number`: Pickup reference number (if available)
  - `pickup_instructions`: Special instructions for pickup
  - `pickup_appointment_start_datetime`: Start time for pickup window
  - `pickup_appointment_end_datetime`: End time for pickup window
- `receiver_section`: Array of receiver information
  - `receiver_company`: Company name
  - `receiver_address`: Full address
  - `receiver_delivery_number`: Delivery reference numbers
  - `receiver_instructions`: Special instructions for delivery
  - `receiver_appointment_start_datetime`: Start time for delivery window
  - `receiver_appointment_end_datetime`: End time for delivery window
- `customer_name`: Name of the customer
- `email_domain`: Email domain (if available)
- `customer_address`: Customer address

## Implementation Approach

1. **Data Loading**
   ```python
   def load_markdown_file(file_path):
       with open(file_path, 'r') as file:
           content = file.read()
       return content
   ```

2. **LLM-Based Extraction**
   ```python
   def extract_data_with_openai(markdown_content):
       client = OpenAI(api_key="provided-api-key")
       
       response = client.chat.completions.create(
           model="gpt-4-1106-preview",
           response_format={"type": "json_object"},
           messages=[
               {"role": "system", "content": """Extract the following information from the provided markdown document:
                - equipment_type
                - reference_number
                - booking_confirmation_number
                - total_rate
                - freight_rate
                - additional_rate
                - shipper_section (array with ship_from_company, ship_from_address, etc.)
                - receiver_section (array with receiver_company, receiver_address, etc.)
                - customer_name
                - email_domain
                - customer_address
                
                Format the response as a JSON object with these fields."""},
               {"role": "user", "content": markdown_content}
           ]
       )
       
       return json.loads(response.choices[0].message.content)
   ```

3. **Post-Processing**
   ```python
   def post_process_extraction(extracted_data):
       # Clean up and format dates consistently
       for shipper in extracted_data.get('shipper_section', []):
           if 'pickup_appointment_start_datetime' in shipper:
               shipper['pickup_appointment_start_datetime'] = format_date(shipper['pickup_appointment_start_datetime'])
           # Similar processing for other date fields
       
       # Format monetary values consistently
       for field in ['total_rate', 'freight_rate', 'additional_rate']:
           if field in extracted_data:
               extracted_data[field] = format_monetary_value(extracted_data[field])
       
       return extracted_data
   ```

4. **Accuracy Evaluation**
   ```python
   def calculate_accuracy(extracted_json, ground_truth_json):
       metrics = {
           'field_presence': 0,  # Percentage of expected fields present
           'field_accuracy': 0,  # Percentage of fields with correct values
           'overall_accuracy': 0  # Weighted combination of above metrics
       }
       
       # Calculate field presence
       expected_fields = get_all_fields(ground_truth_json)
       present_fields = get_all_fields(extracted_json)
       metrics['field_presence'] = len(present_fields.intersection(expected_fields)) / len(expected_fields)
       
       # Calculate field accuracy
       correct_fields = 0
       for field in expected_fields:
           if get_field_value(extracted_json, field) == get_field_value(ground_truth_json, field):
               correct_fields += 1
       
       metrics['field_accuracy'] = correct_fields / len(expected_fields)
       
       # Calculate overall accuracy
       metrics['overall_accuracy'] = 0.4 * metrics['field_presence'] + 0.6 * metrics['field_accuracy']
       
       return metrics
   ```

## Main Pipeline

```python
def main():
    # 1. Set up paths
    markdown_dir = "hackathon_dataset_organized/markdown"
    extraction_dir = "hackathon_dataset_organized/extraction"
    output_dir = "our_extraction_results"
    
    # 2. Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # 3. Process each markdown file
    markdown_files = glob.glob(os.path.join(markdown_dir, "*.md"))
    
    results = []
    for md_file in markdown_files:
        # Extract file ID
        file_id = os.path.basename(md_file).split('.')[0]
        
        # Load markdown content
        markdown_content = load_markdown_file(md_file)
        
        # Extract data using OpenAI
        extracted_data = extract_data_with_openai(markdown_content)
        
        # Post-process the extracted data
        processed_data = post_process_extraction(extracted_data)
        
        # Save the extraction result
        output_file = os.path.join(output_dir, f"{file_id}_extraction.json")
        with open(output_file, 'w') as f:
            json.dump(processed_data, f, indent=2)
        
        # Calculate accuracy if ground truth exists
        ground_truth_file = os.path.join(extraction_dir, f"{file_id}_extraction.json")
        if os.path.exists(ground_truth_file):
            with open(ground_truth_file, 'r') as f:
                ground_truth = json.load(f)
            
            accuracy = calculate_accuracy(processed_data, ground_truth)
            results.append({
                'file_id': file_id,
                'accuracy': accuracy
            })
    
    # 4. Generate accuracy report
    generate_accuracy_report(results)
```

## Accuracy Metrics

We will define accuracy based on the following metrics:

1. **Field Presence**: Percentage of expected fields that are present in our extraction
2. **Field Accuracy**: Percentage of fields with values that match the ground truth
3. **Overall Accuracy**: Weighted combination of field presence and field accuracy

For complex fields like arrays (shipper_section, receiver_section), we'll calculate accuracy for each item and average them.

## Challenges and Considerations

1. **Date Format Consistency**: Ensuring dates are formatted consistently (MM/DD/YY HH:MM)
2. **Address Parsing**: Correctly separating address components
3. **Handling Missing Data**: Some fields may not be explicitly mentioned in the markdown
4. **Monetary Value Formatting**: Ensuring consistent decimal precision for monetary values
5. **Instruction Text Extraction**: Properly capturing special instructions that may span multiple lines

## Next Steps

After implementing the extraction pipeline, we will:

1. Run the pipeline on a sample of markdown files
2. Evaluate accuracy against ground truth extraction files
3. Refine the extraction process based on error analysis
4. Scale up to process the entire dataset
5. Prepare for Part 2: Mapping extraction JSON to TMS JSON
