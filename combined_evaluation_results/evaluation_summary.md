# Extraction Evaluation Summary

## Overall Metrics

- **Average Field Presence**: 83.04%
- **Average Field Accuracy (Strict)**: 62.73%
- **Average Field Accuracy (Relaxed)**: 69.94%
- **Critical Fields Accuracy (Strict)**: 65.93%
- **Critical Fields Accuracy (Relaxed)**: 73.55%
- **Average Overall Accuracy**: 75.31%

## Files Processed

- **Total Files**: 85
- **Files with >90% Accuracy**: 7
- **Files with <50% Accuracy**: 5

## Field Analysis

### Critical Fields Performance

| Field | Presence Rate | Strict Accuracy | Relaxed Accuracy |
|-------|--------------|----------------|------------------|
| receiver_section[0].receiver_appointment_start_time | 0.00% | 0.00% | 0.00% |
| receiver_section[0].receiver_appointment_end_time | 0.00% | 0.00% | 0.00% |
| receiver_section[2].receiver_address | 100.00% | 0.00% | 100.00% |
| shipper_section[2].pickup_instructions | 0.00% | 0.00% | 0.00% |
| shipper_section[0].pickup_appointment_date | 0.00% | 0.00% | 0.00% |
| receiver_section[0].receiver_appointment_date | 0.00% | 0.00% | 0.00% |
| shipper_section[0].pickup_appointment_end_time | 0.00% | 0.00% | 0.00% |
| receiver_section[1].receiver_address | 50.00% | 0.00% | 0.00% |
| receiver_section[2].receiver_instructions | 0.00% | 0.00% | 0.00% |
| shipper_section[1].pickup_instructions | 0.00% | 0.00% | 0.00% |
| receiver_section[1].receiver_instructions | 0.00% | 0.00% | 0.00% |
| shipper_section[0].pickup_appointment_start_time | 0.00% | 0.00% | 0.00% |
| receiver_section[0].receiver_instructions | 47.56% | 20.73% | 25.61% |
| shipper_section[0].pickup_instructions | 71.08% | 31.33% | 51.81% |
| receiver_section[0].receiver_delivery_number | 76.83% | 31.71% | 46.34% |
| customer_name | 80.00% | 35.29% | 45.88% |
| shipper_section[0].pickup_number | 66.27% | 37.35% | 40.96% |
| shipper_section[1].pickup_appointment_end_datetime | 40.00% | 40.00% | 40.00% |
| shipper_section[1].pickup_number | 40.00% | 40.00% | 40.00% |
| shipper_section[1].ship_from_company | 40.00% | 40.00% | 40.00% |
| shipper_section[1].ship_from_address | 40.00% | 40.00% | 40.00% |
| shipper_section[1].pickup_appointment_start_datetime | 40.00% | 40.00% | 40.00% |
| receiver_section[1].receiver_appointment_end_datetime | 50.00% | 50.00% | 50.00% |
| receiver_section[1].receiver_company | 50.00% | 50.00% | 50.00% |
| receiver_section[1].receiver_appointment_start_datetime | 50.00% | 50.00% | 50.00% |
| receiver_section[1].receiver_delivery_number | 50.00% | 50.00% | 50.00% |
| shipper_section[0].ship_from_address | 93.98% | 50.60% | 92.77% |
| receiver_section[0].receiver_address | 96.34% | 51.22% | 93.90% |
| equipment_type | 91.76% | 55.29% | 57.65% |
| receiver_section[0].receiver_appointment_end_datetime | 71.95% | 68.29% | 69.51% |
| shipper_section[0].pickup_appointment_end_datetime | 77.11% | 73.49% | 74.70% |
| freight_rate | 90.59% | 81.18% | 81.18% |
| shipper_section[0].ship_from_company | 91.57% | 84.34% | 87.95% |
| booking_confirmation_number | 98.80% | 86.75% | 87.95% |
| shipper_section[0].pickup_appointment_start_datetime | 91.57% | 87.95% | 90.36% |
| receiver_section[0].receiver_company | 96.34% | 89.02% | 92.68% |
| receiver_section[0].receiver_appointment_start_datetime | 93.90% | 90.24% | 91.46% |
| shipper_section | 100.00% | 92.86% | 94.05% |
| total_rate | 95.29% | 92.94% | 92.94% |
| receiver_section | 100.00% | 94.05% | 94.05% |
| reference_number | 98.11% | 94.34% | 96.23% |
| shipper_section[2].ship_from_address | 100.00% | 100.00% | 100.00% |
| shipper_section[2].pickup_appointment_start_datetime | 100.00% | 100.00% | 100.00% |
| shipper_section[2].ship_from_company | 100.00% | 100.00% | 100.00% |
| shipper_section[2].pickup_appointment_end_datetime | 100.00% | 100.00% | 100.00% |
| receiver_section[2].receiver_appointment_start_datetime | 100.00% | 100.00% | 100.00% |
| receiver_section[2].receiver_delivery_number | 100.00% | 100.00% | 100.00% |
| receiver_section[2].receiver_appointment_end_datetime | 100.00% | 100.00% | 100.00% |
| receiver_section[2].receiver_company | 100.00% | 100.00% | 100.00% |
| shipper_section[2].pickup_number | 100.00% | 100.00% | 100.00% |

### Top 10 Most Problematic Fields

| Field | Presence Rate | Strict Accuracy | Relaxed Accuracy |
|-------|--------------|----------------|------------------|
| receiver_section[0].receiver_appointment_start_time | 0.00% | 0.00% | 0.00% |
| receiver_section[1].receiver_instructions | 0.00% | 0.00% | 0.00% |
| shipper_section[1].pickup_instructions | 0.00% | 0.00% | 0.00% |
| receiver_section[2].receiver_instructions | 0.00% | 0.00% | 0.00% |
| receiver_section[1].receiver_address | 50.00% | 0.00% | 0.00% |
| shipper_section[0].pickup_appointment_start_time | 0.00% | 0.00% | 0.00% |
| receiver_section[0].receiver_appointment_date | 0.00% | 0.00% | 0.00% |
| shipper_section[0].pickup_appointment_date | 0.00% | 0.00% | 0.00% |
| shipper_section[2].pickup_instructions | 0.00% | 0.00% | 0.00% |
| receiver_section[2].receiver_address | 100.00% | 0.00% | 100.00% |

### Top 10 Most Reliable Fields

| Field | Presence Rate | Strict Accuracy | Relaxed Accuracy |
|-------|--------------|----------------|------------------|
| shipper_section[2].pickup_number | 100.00% | 100.00% | 100.00% |
| shipper_section[2].pickup_appointment_end_datetime | 100.00% | 100.00% | 100.00% |
| shipper_section[2].ship_from_address | 100.00% | 100.00% | 100.00% |
| shipper_section[2].pickup_appointment_start_datetime | 100.00% | 100.00% | 100.00% |
| shipper_section[2].ship_from_company | 100.00% | 100.00% | 100.00% |
| receiver_section[2].receiver_company | 100.00% | 100.00% | 100.00% |
| receiver_section[2].receiver_appointment_start_datetime | 100.00% | 100.00% | 100.00% |
| receiver_section[2].receiver_delivery_number | 100.00% | 100.00% | 100.00% |
| additional_rates[0].amount | 100.00% | 100.00% | 100.00% |
| receiver_section[2].receiver_appointment_end_datetime | 100.00% | 100.00% | 100.00% |