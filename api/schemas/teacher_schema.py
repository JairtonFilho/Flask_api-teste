from api import ma
from api.models import teacher_model
from marshmallow import fields


class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_model.TeacherModel
        load_instance = True
        fields = ('id', 'name', 'age', '_links')

    name = fields.String(required=True)
    age = fields.Integer(required=True)

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("teacherview", values=dict(id="<id>")),
            "put": ma.URLFor("teacherview", values=dict(id="<id>")),
            "delete": ma.URLFor("teacherview", values=dict(id="<id>"))
        }
    )
