from flask_restful import Resource
from flask import request

from models.user import UserModel
from schemas.user import UserSchema


user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": f"No user found with userID {user_id}"}, 404

        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": f"No user found with userID {user_id}"}, 404

        user.delte_from_db()
        return {"message": "User deleted successfully"}, 200


class UserCreate(Resource):
    @classmethod
    def post(cls):
        user = user_schema.load(request.get_json())

        if UserModel.find_by_email(user.email):
            return {"message": f"User with this {user.email} email already exists"}, 400

        user.save_to_db()

        return user_schema.dump(user), 201


class UserList(Resource):
    @classmethod
    def get(cls):
        return {"users": user_list_schema.dump(UserModel.find_all())}
