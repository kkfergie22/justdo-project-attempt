"""Module for the controller class"""

from flask import jsonify, request
from app.models.tasks import Task


class TaskController:
    """Controller class for tasks management"""
    @staticmethod
    def get_all_tasks():
        tasks = Task.get_all()
        return jsonify(tasks)

    @staticmethod
    def create_task():
        data = request.json
        name = data.get('name')
        description = data.get('description')
        due_date = data.get('due_date')
        category = data.get('category')

        task = Task(name, description, due_date, category)
        task_id = task.save()

        return jsonify({'message': 'Task created successfully',
                        'task_id': task_id})

    @staticmethod
    def get_task(task_id):
        task = Task.get_by_id(task_id)
        if task:
            return jsonify(task)
        else:
            return jsonify({'message': 'Task not found'}), 404

    @staticmethod
    def update_task(task_id):
        task = Task.get_by_id(task_id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404
        data = request.json
        task.name = data.get('name')
        task.description = data.get('description')
        task.due_date = data.get('due_date')
        task.category = data.get('category')
        task.status = data.get('status')
        task.update(task_id)
        return jsonify({'message': 'Task updated', 'Last updated':
                        task.last_updated})

    @staticmethod
    def delete_task(task_id):
        task = Task.get_by_id(task_id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404
        task.delete(task_id)
        return jsonify({'message': 'Task deleted'}), 200

    # def delete_all_tasks():
    #     Task.delete_all()
    #     return jsonify({'message': 'All tasks deleted'}), 200
