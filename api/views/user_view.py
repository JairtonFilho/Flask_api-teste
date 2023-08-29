from flask_restful import Resource
from api import api
from api.schemas import user_schema
from flask import request, make_response, jsonify
from api.entities import user_entity
from api.services import user_service
from flask_jwt_extended import jwt_required


class UserView(Resource):
    @jwt_required()
    def post(self):
        us = user_schema.UserSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            email = request.json['email']
            password = request.json['password']

            new_user = user_entity.UserEntity(name=name, email=email, password=password)
            result = user_service.add_user(new_user)
            serialized_result = us.dump(result)

            return make_response(jsonify(serialized_result), 201)


api.add_resource(UserView, '/user')
