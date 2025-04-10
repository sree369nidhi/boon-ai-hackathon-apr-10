# Part 2: TMS Format Conversion and Comparison Plan

## Overview

In this second part of the hackathon, we need to:
1. Convert our extraction JSON files to the target TMS JSON format
2. Compare our converted TMS files with the provided ground truth TMS files
3. Evaluate the accuracy of our conversion

## Understanding the Task

### Input
- Our extraction JSON files (from Part 1)
- Sample TMS JSON files (ground truth)

### Output
- Converted TMS JSON files in the required format
- Comparison metrics between our TMS files and ground truth TMS files

## Approach

### 1. Analyze TMS Format

First, we need to understand the structure and requirements of the TMS format:
- Examine multiple TMS JSON files to identify patterns and required fields
- Map fields from our extraction format to the TMS format
- Identify any transformations or calculations needed

### 2. Develop Conversion Logic

Create a script that:
- Reads our extraction JSON files
- Transforms the data to match the TMS format
- Handles special cases and edge conditions
- Outputs properly formatted TMS JSON files

### 3. Implement Comparison Metrics

Develop an evaluation script that:
- Compares our converted TMS files with ground truth TMS files
- Calculates accuracy metrics (similar to Part 1)
- Identifies common errors or discrepancies

### 4. Test and Refine

- Test the conversion on a small sample first
- Analyze results and identify issues
- Refine the conversion logic
- Scale to the full dataset

## Implementation Plan

### Phase 1: TMS Format Analysis (1 hour)
- [ ] Examine at least 5 TMS JSON files to understand structure
- [ ] Create a field mapping document (extraction → TMS)
- [ ] Identify required vs. optional fields
- [ ] Document any special formatting or calculation requirements

### Phase 2: Conversion Script Development (2 hours)
- [ ] Create a basic conversion function for core fields
- [ ] Implement handling for complex fields (arrays, nested objects)
- [ ] Add special case handling for edge conditions
- [ ] Implement validation to ensure output matches TMS format

### Phase 3: Comparison Logic (1 hour)
- [ ] Adapt our evaluation approach from Part 1
- [ ] Implement field-by-field comparison with appropriate matching criteria
- [ ] Create metrics for overall conversion accuracy

### Phase 4: Testing and Refinement (1 hour)
- [ ] Test conversion on 10 sample files
- [ ] Compare with ground truth and analyze discrepancies
- [ ] Refine conversion logic
- [ ] Scale to full dataset

## Key Considerations

### Potential Challenges
1. **Field Mapping Complexity**: Some fields may require complex transformations
2. **Missing Data**: Handling cases where required TMS fields don't have corresponding extraction data
3. **Format Variations**: Dealing with variations in the TMS format across different files
4. **Calculation Requirements**: Some TMS fields might require calculations based on multiple extraction fields

### Success Criteria
1. **High Field Presence**: All required TMS fields should be present
2. **Accurate Values**: Field values should match ground truth
3. **Format Compliance**: Output should strictly adhere to TMS format requirements
4. **Scalability**: Solution should handle the entire dataset efficiently

## Next Steps
1. Begin by examining TMS files to understand the target format
2. Create a detailed field mapping document
3. Implement the conversion script
4. Develop comparison metrics
5. Test, evaluate, and refine
