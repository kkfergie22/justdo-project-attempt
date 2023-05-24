import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
