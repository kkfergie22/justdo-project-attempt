from flask import Flask
from pymongo import MongoClient
from config import MONGO_DB_NAME, MONGO_HOST, MONGO_PORT


app = Flask(__name__)

# Establish connection to mongodb

client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/')
db = client[MONGO_DB_NAME]


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
