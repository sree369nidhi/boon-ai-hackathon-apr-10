#!/usr/bin/env python3
"""
Evaluate TMS conversion by comparing converted TMS files with ground truth TMS files.

This script compares the converted TMS files with the ground truth TMS files
to measure the accuracy of the conversion process and identify discrepancies.
"""

import json
import os
import argparse
import glob
from typing import Dict, List, Any, Tuple, Set
import pandas as pd
import matplotlib.pyplot as plt
from difflib import SequenceMatcher

# Critical fields to evaluate
CRITICAL_FIELDS = [
    "blnum",                   # Bill/reference number
    "customer_id",             # Customer ID
    "equipment_type_id",       # Equipment type
    "freight_charge",          # Freight charge
    "total_charge",            # Total charge
    "otherchargetotal",        # Other charges total
    "temperature_min",         # Min temperature (if applicable)
    "temperature_max",         # Max temperature (if applicable)
]

# Stop fields to evaluate
STOP_FIELDS = [
    "address",                 # Street address
    "city_name",               # City
    "state",                   # State
    "zip_code",                # ZIP code
    "location_name",           # Location name
    "stop_type",               # Stop type (PU/SO)
    "sched_arrive_early",      # Scheduled early arrival
    "sched_arrive_late",       # Scheduled late arrival
]

# Fields that can be compared with fuzzy matching
FUZZY_FIELDS = [
    "location_name",
    "address",
]

# Numeric fields that can have a tolerance
NUMERIC_FIELDS = [
    "freight_charge",
    "total_charge",
    "otherchargetotal",
    "temperature_min",
    "temperature_max",
]


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


def is_field_match(field: str, value1: Any, value2: Any, fuzzy_threshold: float = 0.8, 
                  numeric_tolerance: float = 0.05) -> bool:
    """
    Check if two field values match, using appropriate comparison method.
    
    Args:
        field: Field name
        value1: First value
        value2: Second value
        fuzzy_threshold: Threshold for fuzzy matching (0.0 to 1.0)
        numeric_tolerance: Tolerance for numeric comparisons (percentage)
        
    Returns:
        True if values match, False otherwise
    """
    # Handle None values
    if value1 is None and value2 is None:
        return True
    
    # If only one is None, they don't match
    if value1 is None or value2 is None:
        return False
    
    # For fuzzy matching fields
    if field in FUZZY_FIELDS:
        return similar(value1, value2) >= fuzzy_threshold
    
    # For numeric fields with tolerance
    if field in NUMERIC_FIELDS:
        try:
            v1 = float(value1)
            v2 = float(value2)
            
            # If either value is 0, use absolute difference
            if v1 == 0 or v2 == 0:
                return abs(v1 - v2) < 1.0
            
            # Otherwise use percentage difference
            return abs(v1 - v2) / max(abs(v1), abs(v2)) <= numeric_tolerance
        except (ValueError, TypeError):
            # If conversion to float fails, fall back to exact match
            return str(value1) == str(value2)
    
    # Default to exact match
    return str(value1) == str(value2)


def compare_tms_files(converted_file: str, ground_truth_file: str) -> Dict[str, Any]:
    """
    Compare a converted TMS file with its ground truth counterpart.
    
    Args:
        converted_file: Path to converted TMS file
        ground_truth_file: Path to ground truth TMS file
        
    Returns:
        Dictionary with comparison results
    """
    # Load files
    with open(converted_file, 'r') as f:
        converted_data = json.load(f)
    
    with open(ground_truth_file, 'r') as f:
        ground_truth_data = json.load(f)
    
    # Initialize results
    results = {
        "file_name": os.path.basename(converted_file),
        "reference_number": converted_data.get("blnum", ""),
        "field_matches": {},
        "field_mismatches": {},
        "missing_fields": [],
        "extra_fields": [],
        "stop_comparison": [],
        "overall_accuracy": 0.0
    }
    
    # Compare critical fields
    total_fields = 0
    matched_fields = 0
    
    for field in CRITICAL_FIELDS:
        if field in ground_truth_data:
            total_fields += 1
            
            if field in converted_data:
                ground_truth_value = ground_truth_data[field]
                converted_value = converted_data[field]
                
                if is_field_match(field, converted_value, ground_truth_value):
                    results["field_matches"][field] = {
                        "converted": converted_value,
                        "ground_truth": ground_truth_value
                    }
                    matched_fields += 1
                else:
                    results["field_mismatches"][field] = {
                        "converted": converted_value,
                        "ground_truth": ground_truth_value
                    }
            else:
                results["missing_fields"].append(field)
        elif field in converted_data:
            results["extra_fields"].append(field)
    
    # Compare stops
    converted_stops = converted_data.get("stops", [])
    ground_truth_stops = ground_truth_data.get("stops", [])
    
    # Match stops by type and sequence
    for c_stop in converted_stops:
        c_type = c_stop.get("stop_type", "")
        c_seq = c_stop.get("order_sequence", 0)
        
        # Find matching ground truth stop
        matched_gt_stop = None
        for gt_stop in ground_truth_stops:
            gt_type = gt_stop.get("stop_type", "")
            gt_seq = gt_stop.get("order_sequence", 0)
            
            if c_type == gt_type and c_seq == gt_seq:
                matched_gt_stop = gt_stop
                break
        
        if matched_gt_stop:
            stop_comparison = {
                "stop_type": c_type,
                "sequence": c_seq,
                "field_matches": {},
                "field_mismatches": {}
            }
            
            # Compare stop fields
            for field in STOP_FIELDS:
                if field in matched_gt_stop:
                    total_fields += 1
                    
                    if field in c_stop:
                        gt_value = matched_gt_stop[field]
                        c_value = c_stop[field]
                        
                        if is_field_match(field, c_value, gt_value):
                            stop_comparison["field_matches"][field] = {
                                "converted": c_value,
                                "ground_truth": gt_value
                            }
                            matched_fields += 1
                        else:
                            stop_comparison["field_mismatches"][field] = {
                                "converted": c_value,
                                "ground_truth": gt_value
                            }
            
            results["stop_comparison"].append(stop_comparison)
    
    # Calculate overall accuracy
    results["overall_accuracy"] = matched_fields / total_fields if total_fields > 0 else 0.0
    results["matched_fields"] = matched_fields
    results["total_fields"] = total_fields
    
    return results


def evaluate_conversion(converted_dir: str, ground_truth_dir: str) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Evaluate all converted TMS files against ground truth files.
    
    Args:
        converted_dir: Directory containing converted TMS files
        ground_truth_dir: Directory containing ground truth TMS files
        
    Returns:
        Tuple of (list of comparison results, summary statistics)
    """
    # Find all converted TMS files
    converted_files = glob.glob(os.path.join(converted_dir, "*_tms.json"))
    
    results = []
    field_accuracy = {field: {"matches": 0, "total": 0} for field in CRITICAL_FIELDS + STOP_FIELDS}
    
    for converted_file in converted_files:
        # Extract reference number
        file_name = os.path.basename(converted_file)
        reference_number = file_name.split('_')[0]
        
        # Find corresponding ground truth file
        ground_truth_file = os.path.join(ground_truth_dir, file_name)
        
        if os.path.exists(ground_truth_file):
            # Compare files
            comparison = compare_tms_files(converted_file, ground_truth_file)
            results.append(comparison)
            
            # Update field accuracy statistics
            for field in comparison["field_matches"]:
                if field in field_accuracy:
                    field_accuracy[field]["matches"] += 1
                    field_accuracy[field]["total"] += 1
            
            for field in comparison["field_mismatches"]:
                if field in field_accuracy:
                    field_accuracy[field]["total"] += 1
            
            for stop_comparison in comparison["stop_comparison"]:
                for field in stop_comparison["field_matches"]:
                    if field in field_accuracy:
                        field_accuracy[field]["matches"] += 1
                        field_accuracy[field]["total"] += 1
                
                for field in stop_comparison["field_mismatches"]:
                    if field in field_accuracy:
                        field_accuracy[field]["total"] += 1
    
    # Calculate summary statistics
    summary = {
        "total_files": len(results),
        "average_accuracy": sum(r["overall_accuracy"] for r in results) / len(results) if results else 0.0,
        "field_accuracy": {
            field: stats["matches"] / stats["total"] if stats["total"] > 0 else 0.0
            for field, stats in field_accuracy.items()
        }
    }
    
    return results, summary


def generate_report(results: List[Dict[str, Any]], summary: Dict[str, Any], output_file: str):
    """
    Generate a detailed report of the evaluation results.
    
    Args:
        results: List of comparison results
        summary: Summary statistics
        output_file: Path to output report file
    """
    with open(output_file, 'w') as f:
        f.write("# TMS Conversion Evaluation Report\n\n")
        
        # Write summary
        f.write("## Summary\n\n")
        f.write(f"- Total files evaluated: {summary['total_files']}\n")
        f.write(f"- Average accuracy: {summary['average_accuracy']:.2%}\n\n")
        
        # Write field accuracy
        f.write("## Field Accuracy\n\n")
        f.write("| Field | Accuracy |\n")
        f.write("|-------|----------|\n")
        
        for field, accuracy in sorted(summary["field_accuracy"].items(), key=lambda x: x[1], reverse=True):
            f.write(f"| {field} | {accuracy:.2%} |\n")
        
        f.write("\n")
        
        # Write detailed results for each file
        f.write("## Detailed Results\n\n")
        
        for result in sorted(results, key=lambda x: x["overall_accuracy"]):
            f.write(f"### {result['file_name']} (Accuracy: {result['overall_accuracy']:.2%})\n\n")
            
            # Write mismatches
            if result["field_mismatches"]:
                f.write("#### Field Mismatches\n\n")
                f.write("| Field | Converted Value | Ground Truth Value |\n")
                f.write("|-------|----------------|--------------------|\n")
                
                for field, values in result["field_mismatches"].items():
                    f.write(f"| {field} | {values['converted']} | {values['ground_truth']} |\n")
                
                f.write("\n")
            
            # Write stop mismatches
            for i, stop in enumerate(result["stop_comparison"]):
                if stop["field_mismatches"]:
                    f.write(f"#### Stop {i+1} ({stop['stop_type']}, Sequence {stop['sequence']}) Mismatches\n\n")
                    f.write("| Field | Converted Value | Ground Truth Value |\n")
                    f.write("|-------|----------------|--------------------|\n")
                    
                    for field, values in stop["field_mismatches"].items():
                        f.write(f"| {field} | {values['converted']} | {values['ground_truth']} |\n")
                    
                    f.write("\n")
            
            f.write("\n")


def generate_visualizations(summary: Dict[str, Any], output_dir: str):
    """
    Generate visualizations of the evaluation results.
    
    Args:
        summary: Summary statistics
        output_dir: Directory to save visualizations
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Field accuracy bar chart
    field_accuracy = summary["field_accuracy"]
    fields = list(field_accuracy.keys())
    accuracies = list(field_accuracy.values())
    
    # Sort by accuracy
    sorted_indices = sorted(range(len(accuracies)), key=lambda i: accuracies[i])
    fields = [fields[i] for i in sorted_indices]
    accuracies = [accuracies[i] for i in sorted_indices]
    
    plt.figure(figsize=(12, 8))
    bars = plt.barh(fields, accuracies, color='skyblue')
    plt.xlabel('Accuracy')
    plt.ylabel('Field')
    plt.title('Field Accuracy')
    plt.xlim(0, 1.0)
    
    # Add percentage labels
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.01, bar.get_y() + bar.get_height()/2, f'{width:.1%}',
                 ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'field_accuracy.png'))
    plt.close()
    
    # Create a dataframe for critical fields vs stop fields
    critical_accuracy = {field: acc for field, acc in field_accuracy.items() if field in CRITICAL_FIELDS}
    stop_accuracy = {field: acc for field, acc in field_accuracy.items() if field in STOP_FIELDS}
    
    critical_avg = sum(critical_accuracy.values()) / len(critical_accuracy) if critical_accuracy else 0
    stop_avg = sum(stop_accuracy.values()) / len(stop_accuracy) if stop_accuracy else 0
    
    categories = ['Critical Fields', 'Stop Fields']
    avg_accuracies = [critical_avg, stop_avg]
    
    plt.figure(figsize=(8, 6))
    plt.bar(categories, avg_accuracies, color=['#ff9999', '#66b3ff'])
    plt.ylabel('Average Accuracy')
    plt.title('Average Accuracy by Field Category')
    plt.ylim(0, 1.0)
    
    # Add percentage labels
    for i, v in enumerate(avg_accuracies):
        plt.text(i, v + 0.01, f'{v:.1%}', ha='center')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'category_accuracy.png'))
    plt.close()


def main():
    """Main function to parse arguments and evaluate conversion."""
    parser = argparse.ArgumentParser(description="Evaluate TMS conversion against ground truth")
    parser.add_argument("--converted", default="converted_tms",
                        help="Directory containing converted TMS files")
    parser.add_argument("--ground-truth", default="hackathon_dataset_organized/tms",
                        help="Directory containing ground truth TMS files")
    parser.add_argument("--output-report", default="tms_evaluation_report.md",
                        help="Path to output report file")
    parser.add_argument("--output-viz", default="tms_evaluation_viz",
                        help="Directory to save visualizations")
    
    args = parser.parse_args()
    
    print(f"Evaluating TMS conversion: {args.converted} vs {args.ground_truth}")
    results, summary = evaluate_conversion(args.converted, args.ground_truth)
    
    print(f"Generating report: {args.output_report}")
    generate_report(results, summary, args.output_report)
    
    print(f"Generating visualizations: {args.output_viz}")
    generate_visualizations(summary, args.output_viz)
    
    print(f"Evaluation complete. Average accuracy: {summary['average_accuracy']:.2%}")


if __name__ == "__main__":
    main()
