from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from config import MONGO_DB_NAME, MONGO_HOST, MONGO_PORT

# Connect to MongoDB
client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/')
db = client[MONGO_DB_NAME]
user_collection = db.users

user_schema = {
    'name': {'type': str, 'required': True},
    'email': {'type': str, 'required': True},
    'password': {'type': str, 'required': True},
    'tasks': {'type': list, 'default': []},
    'createdAt': {'type': datetime, 'required': True},
    'updatedAt': {'type': datetime}
}


class User:
    """The model for the user"""
    def __init__(self, name, email, password) -> None:
        self.name = name,
        self.email = email,
        self.password = password,
        self.tasks = [],
        self.createdAt = None,
        self.updateAt = None

    def save(self):
        "Saves a user to the database"
        user_data = {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'createdAt': datetime.utcnow(),
            'updatedAt': None
        }
        user_id = user_collection.insert_one(user_data).inserted_id
        return str(user_id)

    @staticmethod
    def get_all():
        "Retrieves a list of all users "
        all_users = list(user_collection.find())
        return all_users

    @staticmethod
    def get_user_by_id(user_id):
        "Retrieves a user by id"
        user = user_collection.find_one({'_id': ObjectId(user_id)})
        return user

    def update_user(self, user_id):
        updated_user_data = {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'updatedAt': datetime.utcnow()
        }
        user_collection.update_one({'_id': ObjectId(user_id)},
                                   {'$set': updated_user_data})

    @staticmethod
    def delete_user(user_id):
        "Deletes a specific user by id"
        user_collection.delete_one({'_id': ObjectId(user_id)})
