from flask_restful import Resource
from flask import request

from models.task import TaskModel
from schemas.task import TaskSchema

task_schema = TaskSchema()


class TaskCreate(Resource):
    @classmethod
    def post(cls):
        task = task_schema.load(request.get_json())
        task.save_to_db()

        return task_schema.dump(task), 201


class Task(Resource):
    @classmethod
    def get(cls, task_id:int):
        task = TaskModel.find_by_id(task_id)

        if not task:
            return {"message": f"Task with taskID {task_id} is not found"}, 404

        return task_schema.dump(task), 200

    @classmethod
    def delete(cls, task_id:int):
        task = TaskModel.find_by_id(task_id)

        if not task:
            return {"message": f"Task with taskID {task_id} is not found"}, 404

        task.delete_from_db()
        return {"message": "Task deleted successfully"}, 200

    @classmethod
    def put(cls, task_id: int):
        task = TaskModel.find_by_id(task_id)

        if not task:
            return {"message": f"Task with taskID {task_id} is not found"}, 404

        task_json = request.get_json()

        task.title = task_json["title"]
        task.description = task_json["description"]

        try:
            task.save_to_db()
        except:
            return {"message": "Unable to update the task"}, 500

        return task_schema.dump(task), 200

