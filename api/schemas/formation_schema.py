from api import ma
from api.models import formation_model
from marshmallow import fields
from api.schemas import course_schema, teacher_schema

class FormationSchema(ma.SQLAlchemyAutoSchema):
    teachers = ma.Nested(teacher_schema.TeacherSchema, many=True, only=('id', 'name'))

    class Meta:
        model = formation_model.FormationModel
        load_instance = True
        fields = ('id', 'name', 'description', 'course', 'teachers', '_links')

    name = fields.String(required=True)
    description = fields.String(required=True)

    course = fields.List(fields.Nested(course_schema.CourseSchema, only=('id', 'name')))

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("formationview", values=dict(id="<id>")),
            "put": ma.URLFor("formationview", values=dict(id="<id>")),
            "delete": ma.URLFor("formationview", values=dict(id="<id>"))
        }
    )

