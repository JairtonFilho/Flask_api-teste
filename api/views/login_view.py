from flask_restful import Resource
from api import api
from api.schemas import login_schema
from flask import request, make_response, jsonify
from api.entities import user_entity
from api.services import user_service
from flask_jwt_extended import create_access_token
from datetime import timedelta


class LoginView(Resource):

    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json['email']
            password = request.json['password']

            user_bd = user_service.get_user_by_email(email)

            if user_bd and user_bd.password_decrypt(password):
                acess_token = create_access_token(identity=user_bd.id,
                                                  expires_delta=timedelta(seconds=100))
                return make_response(jsonify({
                    'token': acess_token,
                    'message': 'Login successful'
                }), 200)

            return make_response(jsonify({
                'message': 'Invalid credentials'
            }), 201)

            serialized_result = ls.dump(result)

            return make_response(jsonify(serialized_result), 201)


api.add_resource(LoginView, '/login')