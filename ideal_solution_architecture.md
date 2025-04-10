# Ideal Two-Step Solution for TMS Conversion

## Overview

This document outlines an ideal two-step solution for converting various document formats into standardized TMS (Transportation Management System) formats, addressing the challenges identified in our current implementation.

## Step 1: PDF to Unified JSON Conversion

### Purpose
Create a standardized intermediate format that serves as the foundation for all downstream conversions.

### Benefits
- **Standardization**: Establishes a consistent, well-defined schema that Boon can maintain and update
- **Training Data**: Creates high-quality mapping examples (M → 1) for fine-tuning LLMs
- **Improved Extraction Accuracy**: Focuses on accurate data extraction without worrying about target-specific formatting
- **Maintainability**: Separates extraction concerns from transformation concerns

### Implementation
1. **Document Ingestion**: Process various document formats (PDF, images, emails, etc.)
2. **OCR & Layout Analysis**: Extract text and understand document structure
3. **Information Extraction**: Use LLMs to extract key fields into a unified JSON schema
4. **Validation**: Apply business rules to validate extracted data
5. **Standardization**: Normalize field formats (dates, addresses, phone numbers, etc.)

### Key Components
- **Unified Schema Definition**: Well-documented JSON schema with clear field definitions
- **Extraction Pipeline**: Modular components for different document types
- **Quality Metrics**: Accuracy tracking for continuous improvement
- **Version Control**: Schema versioning to track changes over time

## Step 2: Unified JSON to TMS-Specific Format

### Purpose
Transform the standardized intermediate format into various TMS-specific formats required by different systems.

### Benefits
- **Flexibility**: Support multiple TMS systems with different requirements
- **Adaptability**: Easily add new TMS formats without changing the extraction process
- **Specialization**: Optimize each conversion for specific TMS requirements
- **Human Oversight**: Incorporate human review for critical or uncertain conversions

### Implementation: Agent-Based System

1. **TMS Format Registry**:
   - Maintain a graph/database of TMS systems and their format requirements
   - Store template formats for each TMS version
   - Track conversion success rates by TMS type

2. **Conversion Agents**:
   - **Rule-Based Agents**: For straightforward, deterministic mappings
   - **LLM-Based Agents**: For complex transformations requiring context understanding
   - **Hybrid Agents**: Combining rules and LLMs for optimal performance

3. **Fallback Mechanism**:
   - **Failure Detection**: Identify when conversion doesn't meet quality thresholds
   - **Human Review Pipeline**: Route failed conversions to human reviewers
   - **Template Creation**: Allow reviewers to create/update templates for new TMS formats
   - **Notification System**: Use services like SendGrid to alert reviewers

4. **Continuous Improvement**:
   - **Feedback Loop**: Incorporate reviewer corrections into training data
   - **Template Evolution**: Update templates based on success/failure patterns
   - **Performance Monitoring**: Track conversion metrics by TMS type, field, and agent

## Architecture Diagram

```
┌───────────────┐    ┌───────────────────┐    ┌───────────────────┐
│               │    │                   │    │                   │
│  Source Docs  │───▶│  Unified JSON     │───▶│  TMS-Specific     │
│  (PDF, etc.)  │    │  (Standard Format)│    │  Format           │
│               │    │                   │    │                   │
└───────────────┘    └───────────────────┘    └───────────────────┘
        │                      │                        │
        ▼                      ▼                        ▼
┌───────────────┐    ┌───────────────────┐    ┌───────────────────┐
│               │    │                   │    │                   │
│  Extraction   │    │  Validation &     │    │  Conversion       │◀─────┐
│  Pipeline     │    │  Standardization  │    │  Agents           │      │
│               │    │                   │    │                   │      │
└───────────────┘    └───────────────────┘    └───────────────────┘      │
                                                       │                  │
                                                       │                  │
                                                       ▼                  │
                                             ┌───────────────────┐        │
                                             │                   │        │
                                             │  Success?         │        │
                                             │                   │        │
                                             └───────────────────┘        │
                                                  │       │               │
                                                  │       │               │
                                             Yes  │       │ No            │
                                                  │       │               │
                                                  ▼       ▼               │
                                 ┌───────────────────┐   ┌───────────────────┐
                                 │                   │   │                   │
                                 │  Deliver to TMS   │   │  Human Review     │
                                 │                   │   │  Pipeline         │
                                 └───────────────────┘   └───────────────────┘
                                                                │
                                                                │
                                                                ▼
                                                      ┌───────────────────┐
                                                      │                   │
                                                      │  Template         │
                                                      │  Creation/Update  │
                                                      │                   │
                                                      └───────────────────┘
                                                                │
                                                                │
                                                                └──────────┘
```

## Implementation Considerations

### 1. Unified JSON Schema Design
- Include all possible fields from various TMS systems
- Use clear, consistent naming conventions
- Support nested structures for complex data (stops, charges, etc.)
- Include metadata about source document and extraction confidence

### 2. TMS Format Registry
- Store format templates as JSON schemas or transformation rules
- Include version information for each TMS system
- Document field mappings and special handling requirements
- Track success rates to identify problematic conversions

### 3. Human Review Interface
- Simple UI for reviewing and correcting conversions
- Template editor for creating/updating TMS formats
- Dashboard for tracking conversion metrics
- Notification system for alerting reviewers

### 4. Performance Metrics
- Conversion accuracy by field and TMS type
- Processing time for each step
- Human review frequency and resolution time
- Template effectiveness over time

## Benefits of This Approach

1. **Scalability**: Add new document types and TMS formats without redesigning the system
2. **Quality**: Focus on accuracy at each specialized step
3. **Adaptability**: Respond to changes in TMS requirements quickly
4. **Learning**: Continuously improve through feedback loops
5. **Efficiency**: Minimize human intervention while maintaining high quality
6. **Transparency**: Clear visibility into conversion performance and issues

## Next Steps

1. Define the unified JSON schema based on comprehensive TMS field analysis
2. Develop and test the extraction pipeline for common document types
3. Create a prototype of the TMS format registry and conversion agents
4. Implement a basic human review interface for failed conversions
5. Establish metrics and monitoring for the end-to-end process
