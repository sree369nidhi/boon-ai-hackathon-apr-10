# In your Python files
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()  # Load .env file

openai_api_key = os.getenv("OPENAI_API_KEY")
# db_endpoint = os.getenv("BOON_DB_ENDPOINT")

logging.info("You have successfully installed the project dependencies. Good to go!")

logging.info(f"OpenAI API Key: {openai_api_key}")

# logging.info(f"DB Endpoint: {db_endpoint}")
