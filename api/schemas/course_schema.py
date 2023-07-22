from api import ma
from api.models import course_model
from marshmallow import fields


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = course_model.CourseModel
        load_instance = True
        fields = ('id', 'name', 'description', 'publication_date', 'formation')

    name = fields.String(required=True)
    description = fields.String(required=True)
    publication_date = fields.Date(required=True)
    formation = fields.String(required=True)
