from typing import List

from db import db


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel")

    @classmethod
    def find_all(cls) -> List["TaskModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, task_id=int) -> "TaskModel":
        return cls.query.filter_by(id=task_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
