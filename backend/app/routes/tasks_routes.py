from flask import Blueprint
from app.controllers.tasks_controller import TaskController

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")
task_controller = TaskController()


@tasks_bp.route('/', methods=['GET'], strict_slashes=False)
def get_all_tasks():
    return task_controller.get_all_tasks()


@tasks_bp.route('/', methods=['POST'], strict_slashes=False)
def create_task():
    return task_controller.create_task()


@tasks_bp.route('/<task_id>', methods=['GET'], strict_slashes=False)
def get_task(task_id):
    return task_controller.get_task(task_id)


@tasks_bp.route('/<task_id>', methods=['PUT'], strict_slashes=False)
def update_task(task_id):
    return task_controller.update_task(task_id)


@tasks_bp.route('/<task_id>', methods=['DELETE'], strict_slashes=False)
def delete_task(task_id):
    return task_controller.delete_task(task_id)

# @tasks_bp.route('/', methods=['DELETE'], strict_slashes=False)
# def delete_all_tasks():
#     Task.delete_all()
#     return jsonify({'message': 'All tasks deleted'}), 200
