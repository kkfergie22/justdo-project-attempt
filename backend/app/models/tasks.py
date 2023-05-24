from datetime import datetime
from pymongo import MongoClient
from config import MONGO_DB_NAME, MONGO_HOST, MONGO_PORT
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/')
db = client[MONGO_DB_NAME]
task_collection = db.tasks

task_schema = {
    'taskName': {'type': str, 'required': True},
    'description': {'type': str},
    'dueDate': {'type': datetime},
    'status': {'type': str, 'default': 'pending'},
    'category': {'type': str}
}


class Task:
    """This is the model for the tasks"""

    def __init__(self, name, description, due_date, category) -> None:
        self.name = name
        self.description = description
        self.due_date = due_date
        self.category = category
        self.status = 'Pending'
        self.created_at = None
        self.last_updated = None

    def save(self):
        task_data = {
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date,
            'status': self.status,
            'category': self.category,
            'created_at': datetime.utcnow(),
            'last_updated': None
        }
        task_id = task_collection.insert_one(task_data).inserted_id
        return str(task_id)

    @staticmethod
    def get_all():
        "Retrieves all tasks from the database"
        all_tasks = list(task_collection.find())
        return all_tasks

    @staticmethod
    def get_by_id(task_id):
        "Retrieves a task from the database by id"
        task = task_collection.find_one({'_id': ObjectId(task_id)})
        return task

    @staticmethod
    def update(self, task_id):
        "Updates a single task by id"
        updated_task = {
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date,
            'status': self.status,
            'category': self.category,
            'last_updated': datetime.utcnow()
        }
        task_collection.update_one({'_id': ObjectId(task_id)},
                                   {'$set': updated_task})

    # @staticmethod
    # def delete_all():
    #     '''Delete all tasks'''
    #     task_collection.delete_many()

    @staticmethod
    def delete(task_id):
        """Deletes a task by id"""
        task_collection.delete_one({'_id': ObjectId(task_id)})
