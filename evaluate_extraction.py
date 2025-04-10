#!/usr/bin/env python3
"""
Extraction Evaluation Script

This script evaluates the accuracy of extraction results by comparing them with
ground truth extraction files. It calculates various metrics and generates a
detailed report.
"""

import os
import json
import glob
import argparse
import pandas as pd
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from collections import defaultdict
from difflib import SequenceMatcher

def load_json_file(file_path):
    """Load content from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def get_all_fields(json_obj, prefix="", field_paths=None):
    """Get all fields in a JSON object recursively."""
    if field_paths is None:
        field_paths = set()
    
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            field_name = f"{prefix}.{key}" if prefix else key
            field_paths.add(field_name)
            
            if isinstance(value, (dict, list)):
                get_all_fields(value, field_name, field_paths)
    
    elif isinstance(json_obj, list):
        for i, item in enumerate(json_obj):
            field_name = f"{prefix}[{i}]"
            get_all_fields(item, field_name, field_paths)
    
    return field_paths

def get_field_value(json_obj, field_path):
    """Get value of a field specified by its path."""
    parts = field_path.split('.')
    current = json_obj
    
    for part in parts:
        # Handle array indexing
        if '[' in part and ']' in part:
            array_name, idx_str = part.split('[', 1)
            idx = int(idx_str.rstrip(']'))
            
            if array_name in current and isinstance(current[array_name], list) and idx < len(current[array_name]):
                current = current[array_name][idx]
            else:
                return None
        else:
            if part in current:
                current = current[part]
            else:
                return None
    
    return current

def similar(a, b):
    """Calculate string similarity ratio between 0 and 1."""
    if not a and not b:  # Both empty
        return 1.0
    if not a or not b:  # One empty
        return 0.0
    return SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio()

def compare_values(ground_truth_value, extracted_value, field_name):
    """Compare two values with appropriate matching based on field type."""
    # Handle None values
    if ground_truth_value is None and extracted_value is None:
        return True, True
    if ground_truth_value is None or extracted_value is None:
        return False, False
    
    # Handle numeric values
    if isinstance(ground_truth_value, (int, float)) or isinstance(extracted_value, (int, float)):
        try:
            # Convert both to float for comparison
            if isinstance(ground_truth_value, str):
                gt_num = float(ground_truth_value.replace(',', '').replace('$', ''))
            else:
                gt_num = float(ground_truth_value)
                
            if isinstance(extracted_value, str):
                ex_num = float(extracted_value.replace(',', '').replace('$', ''))
            else:
                ex_num = float(extracted_value)
                
            # Exact match (within small epsilon)
            exact_match = abs(gt_num - ex_num) < 0.01
            # Relaxed match (within percentage)
            close_match = abs(gt_num - ex_num) < max(1.0, abs(gt_num * 0.1))  # Within 10% or $1
            
            return exact_match, close_match
        except (ValueError, TypeError):
            # If conversion fails, fall back to string comparison
            pass
    
    # Handle boolean values
    if isinstance(ground_truth_value, bool) and isinstance(extracted_value, bool):
        return ground_truth_value == extracted_value, ground_truth_value == extracted_value
    
    # Convert to strings for comparison
    gt_str = str(ground_truth_value).lower().strip()
    ex_str = str(extracted_value).lower().strip()
    
    # Exact match (case-insensitive)
    exact_match = gt_str == ex_str
    
    # Fuzzy matching based on field type
    if 'address' in field_name:
        # For addresses, check if key parts are contained
        similarity = similar(gt_str, ex_str)
        close_match = similarity > 0.7 or gt_str in ex_str or ex_str in gt_str
    elif 'name' in field_name or 'company' in field_name:
        # For names, use higher similarity threshold
        similarity = similar(gt_str, ex_str)
        close_match = similarity > 0.8
    elif 'date' in field_name or 'time' in field_name:
        # For dates/times, check if they contain the same core information
        # Remove common formatting characters
        gt_clean = ''.join(c for c in gt_str if c.isalnum())
        ex_clean = ''.join(c for c in ex_str if c.isalnum())
        similarity = similar(gt_clean, ex_clean)
        close_match = similarity > 0.8
    else:
        # For other strings, use moderate similarity
        similarity = similar(gt_str, ex_str)
        close_match = similarity > 0.85
    
    return exact_match, close_match

def compare_nested_structures(ground_truth_value, extracted_value, parent_field=""):
    """Compare nested structures (lists/dicts) field by field."""
    # If both are dictionaries, compare each field
    if isinstance(ground_truth_value, dict) and isinstance(extracted_value, dict):
        all_keys = set(ground_truth_value.keys()) | set(extracted_value.keys())
        matches = []
        close_matches = []
        
        for key in all_keys:
            field_name = f"{parent_field}.{key}" if parent_field else key
            
            # Skip if key doesn't exist in one of the dictionaries
            if key not in ground_truth_value or key not in extracted_value:
                matches.append(False)
                close_matches.append(False)
                continue
            
            # Recursively compare nested values
            if isinstance(ground_truth_value[key], (dict, list)) and isinstance(extracted_value[key], (dict, list)):
                exact, close = compare_nested_structures(ground_truth_value[key], extracted_value[key], field_name)
                matches.append(exact)
                close_matches.append(close)
            else:
                exact, close = compare_values(ground_truth_value[key], extracted_value[key], field_name)
                matches.append(exact)
                close_matches.append(close)
        
        # Structure matches if all fields match
        return any(matches) and len(matches) > 0, any(close_matches) and len(close_matches) > 0
    
    # If both are lists, compare each item
    elif isinstance(ground_truth_value, list) and isinstance(extracted_value, list):
        # For empty lists
        if not ground_truth_value and not extracted_value:
            return True, True
        if not ground_truth_value or not extracted_value:
            return False, False
            
        # For lists of dictionaries (like shipper_section), compare each item
        if all(isinstance(item, dict) for item in ground_truth_value) and all(isinstance(item, dict) for item in extracted_value):
            # Compare each item in the list with its best match in the other list
            matches = []
            close_matches = []
            
            # For each ground truth item, find the best matching extracted item
            for i, gt_item in enumerate(ground_truth_value):
                best_match = 0
                best_close_match = 0
                
                for ex_item in extracted_value:
                    field_name = f"{parent_field}[{i}]" if parent_field else f"[{i}]"
                    exact, close = compare_nested_structures(gt_item, ex_item, field_name)
                    
                    if exact:
                        best_match = 1
                    if close:
                        best_close_match = 1
                
                matches.append(best_match > 0)
                close_matches.append(best_close_match > 0)
            
            return any(matches), any(close_matches)
        
        # For simple lists, compare values directly
        return ground_truth_value == extracted_value, similar(''.join(map(str, ground_truth_value)), ''.join(map(str, extracted_value))) > 0.7
    
    # If types don't match, compare as strings
    return compare_values(ground_truth_value, extracted_value, parent_field)

def calculate_field_metrics(extracted_json, ground_truth_json):
    """Calculate detailed metrics for each field."""
    field_metrics = {}
    
    # Get all fields from ground truth
    ground_truth_fields = get_all_fields(ground_truth_json)
    
    # Define critical fields that are most important
    critical_fields = [
        'reference_number',
        'booking_confirmation_number',
        'shipper_section',
        'receiver_section',
        'customer_name',
        'equipment_type',
        'total_rate',
        'freight_rate'
    ]
    
    # Special handling for nested structures
    nested_structures = ['shipper_section', 'receiver_section', 'additional_rates']
    
    for field in ground_truth_fields:
        ground_truth_value = get_field_value(ground_truth_json, field)
        extracted_value = get_field_value(extracted_json, field)
        
        # Field presence
        is_present = extracted_value is not None
        
        # Field accuracy (if present)
        is_correct = False
        is_close_match = False
        
        # For nested structures like shipper_section or receiver_section
        if is_present and any(ns in field for ns in nested_structures) and '.' not in field and '[' not in field:
            # Compare the structure field by field
            is_correct, is_close_match = compare_nested_structures(ground_truth_value, extracted_value, field)
        elif is_present:
            # For regular fields, compare values directly
            is_correct, is_close_match = compare_values(ground_truth_value, extracted_value, field)
        
        # Determine if this is a critical field
        is_critical = any(cf in field for cf in critical_fields)
        
        field_metrics[field] = {
            'present': is_present,
            'correct': is_correct,
            'close_match': is_close_match,
            'critical': is_critical
        }
    
    return field_metrics

def calculate_file_accuracy(extracted_json, ground_truth_json):
    """Calculate accuracy metrics for a single file."""
    metrics = {
        'field_presence': 0,  # Percentage of expected fields present
        'field_accuracy': 0,  # Percentage of fields with correct values
        'relaxed_accuracy': 0,  # Percentage including close matches
        'critical_accuracy': 0,  # Accuracy of critical fields only
        'critical_relaxed': 0,  # Relaxed accuracy of critical fields only
        'overall_accuracy': 0  # Weighted combination of metrics
    }
    
    # Calculate detailed metrics for each field
    field_metrics = calculate_field_metrics(extracted_json, ground_truth_json)
    
    total_fields = len(field_metrics)
    if total_fields == 0:
        return metrics, field_metrics
    
    # Count fields by different criteria
    present_fields = sum(1 for metrics in field_metrics.values() if metrics['present'])
    correct_fields = sum(1 for metrics in field_metrics.values() if metrics['correct'])
    close_match_fields = sum(1 for metrics in field_metrics.values() if metrics['correct'] or metrics['close_match'])
    
    # Count critical fields
    critical_fields = [f for f, m in field_metrics.items() if m['critical']]
    critical_present = sum(1 for f in critical_fields if field_metrics[f]['present'])
    critical_correct = sum(1 for f in critical_fields if field_metrics[f]['correct'])
    critical_close = sum(1 for f in critical_fields if field_metrics[f]['correct'] or field_metrics[f]['close_match'])
    
    # Calculate metrics
    metrics['field_presence'] = present_fields / total_fields
    metrics['field_accuracy'] = correct_fields / total_fields
    metrics['relaxed_accuracy'] = close_match_fields / total_fields
    
    # Calculate critical field accuracy
    if critical_fields:
        metrics['critical_accuracy'] = critical_correct / len(critical_fields)
        metrics['critical_relaxed'] = critical_close / len(critical_fields)
    else:
        metrics['critical_accuracy'] = 0
        metrics['critical_relaxed'] = 0
    
    # Calculate weighted overall accuracy
    # 30% field presence, 30% relaxed accuracy, 40% critical field accuracy
    metrics['overall_accuracy'] = (
        0.3 * metrics['field_presence'] + 
        0.3 * metrics['relaxed_accuracy'] + 
        0.4 * metrics['critical_relaxed']
    )
    
    return metrics, field_metrics

def analyze_field_performance(all_field_metrics):
    """Analyze performance across all files for each field."""
    field_performance = defaultdict(lambda: {
        'present_count': 0, 
        'correct_count': 0, 
        'close_match_count': 0,
        'total_count': 0,
        'is_critical': False
    })
    
    for file_id, field_metrics in all_field_metrics.items():
        for field, metrics in field_metrics.items():
            field_performance[field]['total_count'] += 1
            field_performance[field]['is_critical'] = metrics.get('critical', False)
            
            if metrics['present']:
                field_performance[field]['present_count'] += 1
            if metrics['correct']:
                field_performance[field]['correct_count'] += 1
            if metrics.get('close_match', False) or metrics['correct']:
                field_performance[field]['close_match_count'] += 1
    
    # Calculate percentages
    for field, counts in field_performance.items():
        counts['presence_rate'] = counts['present_count'] / counts['total_count'] if counts['total_count'] > 0 else 0
        counts['accuracy_rate'] = counts['correct_count'] / counts['total_count'] if counts['total_count'] > 0 else 0
        counts['close_match_rate'] = counts['close_match_count'] / counts['total_count'] if counts['total_count'] > 0 else 0
    
    return field_performance

def generate_plots(results_df, field_performance, output_dir):
    """Generate visualization plots for the evaluation results."""
    # Create plots directory
    plots_dir = os.path.join(output_dir, 'plots')
    os.makedirs(plots_dir, exist_ok=True)
    
    # 1. Overall accuracy distribution
    plt.figure(figsize=(10, 6))
    plt.hist(results_df['overall_accuracy'], bins=20, alpha=0.7)
    plt.title('Distribution of Overall Accuracy')
    plt.xlabel('Accuracy')
    plt.ylabel('Number of Files')
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(plots_dir, 'overall_accuracy_distribution.png'))
    plt.close()
    
    # 2. Field presence vs. accuracy
    plt.figure(figsize=(10, 6))
    plt.scatter(results_df['field_presence'], results_df['field_accuracy'], alpha=0.5)
    plt.title('Field Presence vs. Field Accuracy')
    plt.xlabel('Field Presence')
    plt.ylabel('Field Accuracy')
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(plots_dir, 'presence_vs_accuracy.png'))
    plt.close()
    
    # 3. Top 20 fields by presence rate
    top_fields_by_presence = sorted(
        [(field, metrics['presence_rate']) for field, metrics in field_performance.items()],
        key=lambda x: x[1],
        reverse=True
    )[:20]
    
    plt.figure(figsize=(12, 8))
    fields, rates = zip(*top_fields_by_presence)
    plt.barh([field.split('.')[-1] for field in fields], rates)
    plt.title('Top 20 Fields by Presence Rate')
    plt.xlabel('Presence Rate')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'top_fields_presence.png'))
    plt.close()
    
    # 4. Bottom 20 fields by accuracy rate
    bottom_fields_by_accuracy = sorted(
        [(field, metrics['accuracy_rate']) for field, metrics in field_performance.items()],
        key=lambda x: x[1]
    )[:20]
    
    plt.figure(figsize=(12, 8))
    fields, rates = zip(*bottom_fields_by_accuracy)
    plt.barh([field.split('.')[-1] for field in fields], rates)
    plt.title('Bottom 20 Fields by Accuracy Rate')
    plt.xlabel('Accuracy Rate')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'bottom_fields_accuracy.png'))
    plt.close()
    
    print(f"Plots saved to {plots_dir}")

def generate_evaluation_report(results, field_performance, output_dir):
    """Generate a comprehensive evaluation report."""
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    
    # Calculate average metrics
    avg_metrics = {
        'field_presence': results_df['field_presence'].mean(),
        'field_accuracy': results_df['field_accuracy'].mean(),
        'relaxed_accuracy': results_df['relaxed_accuracy'].mean() if 'relaxed_accuracy' in results_df else 0,
        'critical_accuracy': results_df['critical_accuracy'].mean() if 'critical_accuracy' in results_df else 0,
        'critical_relaxed': results_df['critical_relaxed'].mean() if 'critical_relaxed' in results_df else 0,
        'overall_accuracy': results_df['overall_accuracy'].mean()
    }
    
    # Save detailed results
    results_df.to_csv(os.path.join(output_dir, "detailed_accuracy.csv"), index=False)
    
    # Convert field performance to DataFrame for analysis
    field_df = pd.DataFrame([
        {
            'field': field,
            'presence_rate': metrics['presence_rate'],
            'accuracy_rate': metrics['accuracy_rate'],
            'close_match_rate': metrics.get('close_match_rate', 0),
            'is_critical': metrics.get('is_critical', False),
            'total_count': metrics['total_count']
        }
        for field, metrics in field_performance.items()
    ])
    
    # Sort by accuracy rate (ascending) to identify problematic fields
    field_df = field_df.sort_values('accuracy_rate')
    field_df.to_csv(os.path.join(output_dir, "field_performance.csv"), index=False)
    
    # Generate summary report
    with open(os.path.join(output_dir, "evaluation_summary.md"), 'w') as f:
        f.write("# Extraction Evaluation Summary\n\n")
        
        f.write("## Overall Metrics\n\n")
        f.write(f"- **Average Field Presence**: {avg_metrics['field_presence']:.2%}\n")
        f.write(f"- **Average Field Accuracy (Strict)**: {avg_metrics['field_accuracy']:.2%}\n")
        f.write(f"- **Average Field Accuracy (Relaxed)**: {avg_metrics['relaxed_accuracy']:.2%}\n")
        f.write(f"- **Critical Fields Accuracy (Strict)**: {avg_metrics['critical_accuracy']:.2%}\n")
        f.write(f"- **Critical Fields Accuracy (Relaxed)**: {avg_metrics['critical_relaxed']:.2%}\n")
        f.write(f"- **Average Overall Accuracy**: {avg_metrics['overall_accuracy']:.2%}\n\n")
        
        f.write("## Files Processed\n\n")
        f.write(f"- **Total Files**: {len(results_df)}\n")
        f.write(f"- **Files with >90% Accuracy**: {len(results_df[results_df['overall_accuracy'] > 0.9])}\n")
        f.write(f"- **Files with <50% Accuracy**: {len(results_df[results_df['overall_accuracy'] < 0.5])}\n\n")
        
        f.write("## Field Analysis\n\n")
        
        # Filter for critical fields
        critical_fields = field_df[field_df['is_critical']].sort_values('accuracy_rate')
        
        f.write("### Critical Fields Performance\n\n")
        f.write("| Field | Presence Rate | Strict Accuracy | Relaxed Accuracy |\n")
        f.write("|-------|--------------|----------------|------------------|");
        
        for _, row in critical_fields.iterrows():
            f.write(f"\n| {row['field']} | {row['presence_rate']:.2%} | {row['accuracy_rate']:.2%} | {row['close_match_rate']:.2%} |")
        
        f.write("\n\n### Top 10 Most Problematic Fields\n\n")
        f.write("| Field | Presence Rate | Strict Accuracy | Relaxed Accuracy |\n")
        f.write("|-------|--------------|----------------|------------------|");
        
        for _, row in field_df.head(10).iterrows():
            f.write(f"\n| {row['field']} | {row['presence_rate']:.2%} | {row['accuracy_rate']:.2%} | {row['close_match_rate']:.2%} |")
        
        f.write("\n\n### Top 10 Most Reliable Fields\n\n")
        f.write("| Field | Presence Rate | Strict Accuracy | Relaxed Accuracy |\n")
        f.write("|-------|--------------|----------------|------------------|");
        
        for _, row in field_df.sort_values('accuracy_rate', ascending=False).head(10).iterrows():
            f.write(f"\n| {row['field']} | {row['presence_rate']:.2%} | {row['accuracy_rate']:.2%} | {row['close_match_rate']:.2%} |")
    
    # Generate plots
    generate_plots(results_df, field_performance, output_dir)
    
    print("\nEvaluation Report:")
    print(f"Average Field Presence: {avg_metrics['field_presence']:.2%}")
    print(f"Average Field Accuracy (Strict): {avg_metrics['field_accuracy']:.2%}")
    print(f"Average Field Accuracy (Relaxed): {avg_metrics['relaxed_accuracy']:.2%}")
    print(f"Critical Fields Accuracy (Strict): {avg_metrics['critical_accuracy']:.2%}")
    print(f"Critical Fields Accuracy (Relaxed): {avg_metrics['critical_relaxed']:.2%}")
    print(f"Average Field Accuracy: {avg_metrics['field_accuracy']:.2%}")
    print(f"Average Overall Accuracy: {avg_metrics['overall_accuracy']:.2%}")
    print(f"Detailed results saved to {output_dir}")
    
    return avg_metrics, results_df, field_df

def main():
    parser = argparse.ArgumentParser(description='Evaluate extraction results against ground truth')
    parser.add_argument('--extraction-dir', default='our_extraction_results', 
                        help='Directory containing extraction results')
    parser.add_argument('--ground-truth-dir', default='hackathon_dataset_organized/extraction', 
                        help='Directory containing ground truth extraction files')
    parser.add_argument('--output-dir', default='evaluation_results', 
                        help='Directory to save evaluation results')
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Get all extraction files
    extraction_files = glob.glob(os.path.join(args.extraction_dir, "*_extraction.json"))
    
    results = []
    all_field_metrics = {}
    
    for ext_file in tqdm(extraction_files, desc="Evaluating files"):
        # Extract file ID
        file_id = os.path.basename(ext_file).split('_')[0]
        
        # Get corresponding ground truth file
        gt_file = os.path.join(args.ground_truth_dir, f"{file_id}_extraction.json")
        
        if not os.path.exists(gt_file):
            print(f"Warning: Ground truth file not found for {file_id}")
            continue
        
        # Load files
        extracted_json = load_json_file(ext_file)
        ground_truth_json = load_json_file(gt_file)
        
        if not extracted_json or not ground_truth_json:
            continue
        
        # Calculate accuracy
        accuracy, field_metrics = calculate_file_accuracy(extracted_json, ground_truth_json)
        
        results.append({
            'file_id': file_id,
            'field_presence': accuracy['field_presence'],
            'field_accuracy': accuracy['field_accuracy'],
            'relaxed_accuracy': accuracy['relaxed_accuracy'],
            'critical_accuracy': accuracy['critical_accuracy'],
            'critical_relaxed': accuracy['critical_relaxed'],
            'overall_accuracy': accuracy['overall_accuracy']
        })
        
        all_field_metrics[file_id] = field_metrics
    
    # Analyze field performance
    field_performance = analyze_field_performance(all_field_metrics)
    
    # Generate evaluation report
    generate_evaluation_report(results, field_performance, args.output_dir)

if __name__ == "__main__":
    main()
