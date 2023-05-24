from flask import jsonify, request
from pymongo import MongoClient
from app import app


@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    """Get all tasks from the database."""
    # Get all tasks from the database.
    tasks = list(tasks_collection.find())
    # Close the database connection.
    client.close()
    # Return the tasks in JSON format.
    return jsonify(tasks), 200


@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task in the database."""
    # Get the task data from the request body.
    data = request.get_json()
    # Create a new task document.
    new_task = {
        'title': data['title'],
        'description': data['description'],
        'due_date': data['due_date'],
        'status': 'Pending',
        'category': data.get('category', '')
    }
    # Insert the task document to the database.
    result = tasks_collection.insert_one(new_task)
    # Get the task from the database.
    task = tasks_collection.find_one({'_id': result.inserted_id})
    # Close the database connection.
    client.close()
    # Return the newly created task in JSON format.
    return jsonify(task), 201


@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    """Get a single task from the database."""
    # Get the task from the database.
    task = tasks_collection.find_one({'_id': id})
    # Close the database connection.
    client.close()
    # Return the task in JSON format.
    return jsonify(task), 200


@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    """Update a task in the database."""
    # Get the task data from the request body.
    data = request.get_json()

    # Update the task in the database.
    tasks_collection.update_one({'_id': id}, {'$set': {
        'title': data['title'],
        'description': data['description'],
        'is_completed': data['is_completed']
    }})

    # Close the database connection.
    client.close()
    # Return a success message.
    return jsonify({'message': 'Task updated successfully!'}), 200


@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    """Delete a task from the database."""
    # Delete the task from the database.
    tasks_collection.delete_one({'_id': id})
    # Close the database connection.
    client.close()
    # Return a success message.
    return jsonify({'message': 'Task deleted successfully!'}), 200
