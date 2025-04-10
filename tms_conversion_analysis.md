# TMS Conversion Analysis

## Overview

This document analyzes the results of converting our extracted JSON files to the target TMS format. We've successfully converted 85 extraction files and evaluated them against the ground truth TMS files to measure accuracy and identify areas for improvement.

## Conversion Process

Our conversion process involved:

1. **Field Mapping**: Creating a comprehensive mapping between extraction fields and TMS fields
2. **Data Transformation**: Converting data formats, parsing addresses, and generating IDs
3. **Validation**: Ensuring the output matches TMS requirements
4. **Evaluation**: Comparing converted files with ground truth files

## Evaluation Results

The evaluation shows an overall average accuracy of **61.34%** across all fields. However, accuracy varies significantly by field type:

### Field Accuracy Breakdown

| Field Type | Field | Accuracy |
|------------|-------|----------|
| **Core Order Fields** | blnum (reference number) | 91.76% |
|  | customer_id | 0.00% |
|  | equipment_type_id | 94.12% |
|  | freight_charge | 85.88% |
|  | total_charge | 92.94% |
|  | otherchargetotal | 87.06% |
| **Temperature Fields** | temperature_min | 31.25% |
|  | temperature_max | 30.00% |
| **Stop Fields** | stop_type | 100.00% |
|  | address | 66.67% |
|  | city_name | 12.35% |
|  | state | 96.91% |
|  | zip_code | 69.14% |
|  | location_name | 29.63% |
|  | sched_arrive_early | 83.44% |
|  | sched_arrive_late | 71.88% |

### Key Observations

1. **Strong Performance Areas**:
   - Stop type identification (100%)
   - Equipment type mapping (94.12%)
   - Reference number mapping (91.76%)
   - Total charge calculation (92.94%)
   - State identification (96.91%)

2. **Weak Performance Areas**:
   - Customer ID mapping (0%)
   - City name extraction (12.35%)
   - Location name mapping (29.63%)
   - Temperature fields (30-31%)

## Analysis of Issues

### 1. Customer ID Mapping (0% Accuracy)

The customer ID field shows 0% accuracy because:
- Our extraction doesn't capture the specific customer ID codes used in the TMS system
- Our simple approach of using the first letters of customer names doesn't match the actual ID scheme
- The TMS likely uses a predefined lookup table for customer IDs

### 2. Address Component Extraction (12-69% Accuracy)

Address parsing shows mixed results:
- State extraction works well (96.91%)
- ZIP code extraction is moderate (69.14%)
- Street address extraction is moderate (66.67%)
- City name extraction is poor (12.35%)

This suggests our regex-based address parsing needs improvement, particularly for city extraction.

### 3. Location Name Mapping (29.63% Accuracy)

The low accuracy for location names indicates:
- Differences in formatting between extraction and TMS
- Possible abbreviations or standardized names in TMS
- Need for a location name lookup/normalization system

### 4. Temperature Fields (30-31% Accuracy)

Temperature fields show low accuracy because:
- Temperature data may be formatted differently in TMS
- Our extraction may not capture all temperature-related information
- Temperature ranges vs. specific values may be handled differently

## Recommendations for Improvement

### 1. Customer ID Mapping

- Create a comprehensive lookup table mapping customer names to their TMS IDs
- Implement fuzzy matching for customer names to handle variations
- Consider using additional identifiers (like address or email domain) to improve matching

### 2. Address Parsing

- Implement a more sophisticated address parsing system
- Use a dedicated address parsing library like `usaddress` or `pyaddress`
- Consider using geocoding services for address standardization
- Implement city name normalization with a reference database

### 3. Location Name Standardization

- Create a mapping table for location names
- Implement fuzzy matching for location names
- Extract and use location codes if available in the original documents

### 4. Temperature Handling

- Standardize temperature format and units
- Improve extraction of temperature-related fields
- Implement proper handling of temperature ranges vs. specific values

### 5. Date and Time Formatting

- Enhance timestamp parsing to handle various formats
- Implement proper timezone handling
- Ensure consistent formatting across all date/time fields

## Implementation Plan

### Phase 1: Address Parsing Enhancement

1. Integrate a dedicated address parsing library
2. Implement address standardization
3. Improve city name extraction and validation
4. Re-evaluate address field accuracy

### Phase 2: Customer and Location Mapping

1. Create reference tables for customer IDs and location names
2. Implement fuzzy matching for names
3. Add contextual clues for better matching
4. Re-evaluate customer ID and location name accuracy

### Phase 3: Temperature and Special Fields

1. Enhance temperature field extraction and conversion
2. Standardize units and formats
3. Implement special field handling for edge cases
4. Re-evaluate temperature field accuracy

## Conclusion

The TMS conversion process shows promising results in several key areas but requires targeted improvements in customer ID mapping, address parsing, and location name standardization. By implementing the recommended enhancements, we can significantly improve the overall accuracy of the conversion process.

The current implementation provides a solid foundation that can be iteratively improved to achieve higher accuracy levels. The modular design of our conversion script makes it straightforward to enhance specific components without affecting the overall structure.
