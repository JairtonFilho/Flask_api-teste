from api import ma
from api.models import user_model
from marshmallow import fields


class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.UserModel
        load_instance = True
        fields = ('id', 'name', 'email', 'password')

    name = fields.String(required=False)
    email = fields.String(required=True)
    password = fields.String(required=True)