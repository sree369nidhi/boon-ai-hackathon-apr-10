# Boon AI Hackathon Project

## Prerequisites
- Python 3.10 or higher
- Poetry (for dependency management) or pip

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

### 3. Install Dependencies

#### Option 1: Using Poetry (Recommended)
```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install
```

#### Option 2: Using pip
```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Running the Code

#### With Poetry
```bash
poetry run python src/test.py
```

#### With pip (if using virtual environment)
```bash
python src/test.py
```

## Project Structure
```
boon-ai-hackathon-apr-10/
├── src/
│   └── test.py          # Main application file
├── .env                 # Environment variables (create this)
├── pyproject.toml       # Poetry project configuration
├── requirements.txt     # pip requirements file
└── README.md           # This file
```

## Troubleshooting
- Make sure all environment variables are properly set in the `.env` file
- If using Poetry, ensure you're using Python 3.10 or higher
- Check that all dependencies are installed correctly

## License
[Add your license information here]