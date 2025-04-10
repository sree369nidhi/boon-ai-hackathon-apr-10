# Boon AI Hackathon Project

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

# Run the code
python src/test.py
```

## Project Structure
```
boon-ai-hackathon-apr-10/
├── src/
│   └── test.py          # Main application file
├── .env                 # Environment variables (create this)
├── pyproject.toml       # Poetry project configuration
├── poetry.lock         # Poetry lock file (dependency versions)
├── requirements.txt     # pip requirements file
└── README.md           # This file
```

## Troubleshooting
- Make sure all environment variables are properly set in the `.env` file
- If using Poetry, ensure you're using Python 3.10 or higher
- Check that all dependencies are installed correctly

## License
[Add your license information here]