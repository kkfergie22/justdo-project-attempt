from flask import Flask
from pymongo import MongoClient
from config import MONGO_DB_NAME, MONGO_HOST, MONGO_PORT
from app.routes.tasks_routes import tasks_bp
import logging

app = Flask(__name__)

app.register_blueprint(tasks_bp)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Configure a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define the log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

# Establish connection to mongodb
try:
    client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/')
    db = client[MONGO_DB_NAME]
    logger.info("Successfully connected to MongoDB")

    # create collections
    tasks_collection = db["tasks"]
    users_collection = db["users"]

except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {str(e)}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
