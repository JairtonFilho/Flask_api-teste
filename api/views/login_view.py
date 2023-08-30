from flask_restful import Resource
from api import api, jwt
from api.schemas import login_schema
from flask import request, make_response, jsonify
from api.services import user_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


class LoginView(Resource):
    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        user_token = user_service.get_user_by_id(identity)
        if user_token.is_admin:
            roles = 'admin'
        else:
            roles = 'user'

        return {'roles':roles}
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
                acess_token = create_access_token(
                    identity=user_bd.id,
                    expires_delta=timedelta(seconds=100)
                )

                refresh_token = create_refresh_token(
                    identity=user_bd.id
                )

                return make_response(jsonify({
                    'token': acess_token,
                    'refresh_token': refresh_token,
                    'message': 'Login successful'
                }), 200)

            return make_response(jsonify({
                'message': 'Invalid credentials'
            }), 401)


api.add_resource(LoginView, '/login')