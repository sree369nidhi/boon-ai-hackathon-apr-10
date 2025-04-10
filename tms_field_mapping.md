# TMS Format Field Mapping

## Overview

This document maps fields from our extraction JSON format to the target TMS JSON format. It serves as a guide for developing the conversion script.

## Core Order Fields

| TMS Field | Extraction Field | Transformation | Notes |
|-----------|------------------|----------------|-------|
| `__type` | N/A | Set to "orders" | Constant value |
| `company_id` | N/A | Set to "TMS" | Constant value |
| `blnum` | `reference_number` | Direct mapping | |
| `customer_id` | `customer_name` | Convert to ID format | May need lookup table |
| `collection_method` | N/A | Set to "P" (Prepaid) | Default value |
| `commodity` | N/A | Set to "DRY" | Default value |
| `commodity_id` | N/A | Set to "DRY" | Default value |
| `equipment_type_id` | `equipment_type` | Map to code | Need mapping table |
| `status` | N/A | Set to "A" | Default value |
| `bill_distance` | Calculate from stops | Sum distances | |
| `bill_distance_um` | N/A | Set to "MI" | Default value |
| `freight_charge` | `freight_rate` or `total_rate` | Direct mapping | |
| `total_charge` | `total_rate` | Direct mapping | |
| `rate` | `freight_rate` | Direct mapping | |
| `rate_type` | `is_flat_rate` | "F" if true | "F" for flat rate |
| `ordered_date` | Current timestamp | Format: "YYYYMMDDHHmmss-0700" | |
| `ordered_method` | N/A | Set to "M" | Default value |
| `operational_status` | N/A | Set to "CLIN" | Default value |
| `order_mode` | N/A | Set to "T" | Default value |

## Temperature Fields

| TMS Field | Extraction Field | Transformation | Notes |
|-----------|------------------|----------------|-------|
| `temperature_min` | `temperature_low` | Direct mapping | Only if temperature_present is true |
| `temperature_max` | `temperature_high` | Direct mapping | Only if temperature_present is true |
| `setpoint_temp` | Calculate | Average of min/max | Only if temperature_present is true |

## Stop Fields

For each stop in the `shipper_section` and `receiver_section` arrays:

| TMS Field | Extraction Field | Transformation | Notes |
|-----------|------------------|----------------|-------|
| `__type` | N/A | Set to "stop" | Constant value |
| `company_id` | N/A | Set to "TMS" | Constant value |
| `address` | `ship_from_address` or `receiver_address` | Extract street address | Parse address |
| `city_name` | `ship_from_address` or `receiver_address` | Extract city | Parse address |
| `state` | `ship_from_address` or `receiver_address` | Extract state | Parse address |
| `zip_code` | `ship_from_address` or `receiver_address` | Extract zip | Parse address |
| `location_name` | `ship_from_company` or `receiver_company` | Direct mapping | |
| `stop_type` | Based on section | "PU" for shipper, "SO" for receiver | |
| `sched_arrive_early` | `pickup_appointment_start_datetime` or `receiver_appointment_start_datetime` | Format timestamp | YYYYMMDDHHmmss-0700 |
| `sched_arrive_late` | `pickup_appointment_end_datetime` or `receiver_appointment_end_datetime` | Format timestamp | YYYYMMDDHHmmss-0700 |
| `driver_load_unload` | N/A | Set to "N" | Default value |
| `status` | N/A | Set to "A" | Default value |

## Reference Numbers

For each stop that has reference numbers:

| TMS Field | Extraction Field | Transformation | Notes |
|-----------|------------------|----------------|-------|
| `__type` | N/A | Set to "reference_number" | Constant value |
| `company_id` | N/A | Set to "TMS" | Constant value |
| `reference_number` | `pickup_number` or `receiver_delivery_number` | Direct mapping | |
| `reference_qual` | N/A | Set to "ON" for delivery, "POL" for pickup | Default values |
| `send_to_driver` | N/A | Set to true | Default value |

## Stop Notes

For stops with instructions:

| TMS Field | Extraction Field | Transformation | Notes |
|-----------|------------------|----------------|-------|
| `__type` | N/A | Set to "stop_note" | Constant value |
| `company_id` | N/A | Set to "TMS" | Constant value |
| `comment_type` | N/A | Set to "DC" | Default value |
| `comments` | `pickup_instructions` or `receiver_instructions` | Direct mapping | |
| `sequence` | N/A | Set to 1 | Default value |
| `system_added` | N/A | Set to false | Default value |

## Movement Fields

For each pair of consecutive stops:

| TMS Field | Extraction Field | Transformation | Notes |
|-----------|------------------|----------------|-------|
| `__type` | N/A | Set to "movement" | Constant value |
| `company_id` | N/A | Set to "TMS" | Constant value |
| `origin_stop_id` | Generated | Use stop ID | |
| `dest_stop_id` | Generated | Use stop ID | |
| `loaded` | N/A | Set to "L" | Default value |
| `movement_type` | N/A | Set to "TKLD" | Default value |
| `status` | N/A | Set to "A" | Default value |
| `move_distance` | Calculate | Distance between stops | May need geocoding |
| `move_distance_um` | N/A | Set to "MI" | Default value |
| `authorized` | N/A | Set to true | Default value |

## Other Charges

For each item in `additional_rates`:

| TMS Field | Extraction Field | Transformation | Notes |
|-----------|------------------|----------------|-------|
| `otherchargetotal` | Sum of `additional_rates[].amount` | Calculate sum | |
| `otherchargetotal_c` | N/A | Set to "USD" | Default value |

## Special Considerations

1. **ID Generation**: TMS format uses unique IDs for stops, movements, and reference numbers. We'll need to generate these consistently.

2. **Address Parsing**: We'll need to parse full addresses into components (street, city, state, zip).

3. **Distance Calculation**: For accurate bill_distance and move_distance, we may need to use geocoding services.

4. **Customer ID Mapping**: We may need a lookup table to convert customer names to their corresponding IDs in the TMS system.

5. **Equipment Type Mapping**: Convert descriptive equipment types to TMS codes.

6. **Timestamp Formatting**: Ensure all timestamps follow the TMS format (YYYYMMDDHHmmss-0700).

7. **Default Values**: Many TMS fields require default values that aren't present in our extraction format.

## Implementation Approach

1. Create a function to parse addresses into components
2. Build a mapping function for equipment types and customer IDs
3. Implement ID generation for various entities
4. Create a main conversion function that:
   - Maps core order fields
   - Processes stops from shipper and receiver sections
   - Generates movements between stops
   - Calculates distances and totals
   - Formats all timestamps correctly
5. Add validation to ensure the output matches TMS requirements
