from ma import ma
from models.task import TaskModel


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TaskModel
        include_fk = True
        dump_only = ("id",)
        load_only = ("user",)
        load_instance = True
