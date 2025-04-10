# Boon AI Hackathon Project - TMS Conversion Solution

## Prerequisites
- Python 3.10 or higher
- Poetry (for dependency management)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sree369nidhi/boon-ai-hackathon-apr-10.git
cd boon-ai-hackathon-apr-10
```

### 2. Set up Environment Variables
Create a `.env` file in the root directory with the following variables:
```env
OPENAI_API_KEY=your_openai_api_key_here
BOON_DB_ENDPOINT=your_db_endpoint_here
```

### 3. Set Up Virtual Environment and Install Dependencies

```bash
# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install Poetry in the virtual environment
pip install poetry

# Install project dependencies using Poetry
poetry install
```

### 4. Running the Code

```bash
# Make sure your virtual environment is activated
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Part 1: Extract data from markdown to unified JSON
python extract_markdown.py

# Evaluate Part 1 extraction results
python evaluate_extraction.py

# Part 2: Convert unified JSON to TMS format (sequential)
python llm_convert_to_tms.py

# OR Part 2: Convert unified JSON to TMS format (parallel - faster)
python parallel_llm_convert.py --workers 10

# Evaluate Part 2 conversion results
python evaluate_llm_conversion.py
```

## Project Overview

This project implements a two-step conversion process for transforming shipping documents into standardized TMS (Transportation Management System) format:

### Part 1: Markdown to Unified JSON Conversion
The first step extracts structured data from markdown files and converts it into a standardized unified JSON format.

- **Script**: `extract_markdown.py`
- **Input**: Markdown files containing shipping information
- **Output**: Unified JSON format in `combined_extraction_results/`
- **Key Features**: 
  - Uses OpenAI API to extract structured data from unstructured text
  - Standardizes field names and formats
  - Creates a consistent intermediate representation

### Part 2: Unified JSON to TMS Format Conversion
The second step transforms the unified JSON data into the specific TMS format required by the target system.

- **Scripts**: `llm_convert_to_tms.py` and `parallel_llm_convert.py`
- **Input**: Unified JSON files from Part 1
- **Output**: TMS-formatted JSON in `llm_converted_tms/`
- **Key Features**:
  - Uses LLM to intelligently map fields to TMS format
  - Handles complex field transformations
  - Supports parallel processing for faster conversion
  - Customer ID mapping for consistent identification

### Evaluation
Both steps of the process are evaluated:

#### Part 1 Evaluation
- **Script**: `evaluate_extraction.py`
- **Output**: Detailed extraction evaluation report
- **Purpose**: Measures accuracy of extracting structured data from markdown files

#### Part 2 Evaluation
- **Script**: `evaluate_llm_conversion.py`
- **Output**: Detailed conversion evaluation report in `llm_tms_evaluation_report.md`
- **Visualizations**: Generated in `llm_tms_evaluation_viz/`
- **Purpose**: Measures accuracy of converting unified JSON to TMS format

## Project Structure
```
boon-ai-hackathon-apr-10/
├── extract_markdown.py              # Part 1: Extract data from markdown to unified JSON
├── evaluate_extraction.py           # Evaluate Part 1 extraction quality
├── llm_convert_to_tms.py            # Part 2: Convert unified JSON to TMS format
├── parallel_llm_convert.py          # Parallel version of the TMS conversion
├── evaluate_llm_conversion.py       # Evaluate Part 2 conversion quality
├── customer_id_mapping.json         # Mapping of customer names to IDs
├── combined_extraction_results/     # Unified JSON output from Part 1
├── llm_converted_tms/               # TMS format output from Part 2
├── hackathon_dataset_organized/     # Original dataset
│   ├── extraction/                  # Extraction files
│   ├── markdown/                    # Markdown files
│   └── tms/                         # Ground truth TMS files
├── llm_tms_evaluation_report.md     # Evaluation results
├── llm_conversion_analysis_report.md # Analysis of conversion performance
├── ideal_solution_architecture.md   # Proposed architecture for production
├── .env                             # Environment variables (create this)
└── README.md                        # This file
```

## Troubleshooting
- Make sure all environment variables are properly set in the `.env` file (especially OPENAI_API_KEY)
- If using Poetry, ensure you're using Python 3.10 or higher
- Check that all dependencies are installed correctly
- If you encounter OpenAI API errors, verify your API key and check for rate limiting
- For parallel processing, adjust the number of workers based on your system's capabilities

## Results

The LLM-based TMS conversion achieved an overall accuracy of 61.35% across 85 files. Key strengths include:
- Perfect handling of stop types (100% accuracy)
- Excellent equipment type identification (95.12%)
- Strong state field accuracy (94.19%)

Areas for improvement:
- Customer ID mapping (2.35% accuracy)
- Temperature fields (0% accuracy)
- Location name formatting (28.39% accuracy)

See `llm_conversion_analysis_report.md` for detailed analysis and recommendations.

## Future Improvements

See `ideal_solution_architecture.md` for a detailed proposal of a production-ready two-step solution with:
- Enhanced customer ID mapping
- Improved address and location formatting
- Temperature field handling
- Post-processing pipeline for standardization
- Human review integration for edge cases

## License
MIT