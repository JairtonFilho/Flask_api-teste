from api import ma
from api.models import teacher_model
from marshmallow import fields


class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_model.TeacherModel
        load_instance = True
        fields = ('id', 'name', 'age')

    name = fields.String(required=True)
    age = fields.Integer(required=True)
