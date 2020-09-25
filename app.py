from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from db import db
from ma import ma
from resources.user import User, UserCreate, UserList
from resources.task import Task, TaskCreate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_err(err):
    return jsonify(err.messages), 400


api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserCreate, "/user")
api.add_resource(UserList, "/users")
api.add_resource(Task, "/task/<int:task_id>")
api.add_resource(TaskCreate, "/task")

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True, port=5000)
