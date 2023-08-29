from flask_restful import Resource
from api import api
from api.schemas import formation_schema
from flask import request, make_response, jsonify
from api.entities import formation_entity
from api.services import formation_service
from api.paginate import paginate
from api.models.formation_model import FormationModel
from flask_jwt_extended import jwt_required


class FormationView(Resource):
    @jwt_required()
    def get(self):
        fs = formation_schema.FormationSchema(many=True)
        return paginate(FormationModel, fs)

    @jwt_required()
    def post(self):
        fs = formation_schema.FormationSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            description = request.json['description']
            teachers = request.json['teachers']

            new_formation = formation_entity.FormationEntity(name=name, description=description, teachers=teachers)
            result = formation_service.add_formation(new_formation)
            serialized_result = fs.dump(result)

            return make_response(jsonify(serialized_result), 201)


class FormationByIdView(Resource):
    @jwt_required()
    def get(self, id):
        result = formation_service.get_formation_by_id(id)
        if not result:
            return make_response(jsonify({'error': 'Formation not found'}), 404)
        else:
            fs = formation_schema.FormationSchema()

        serialized_result = fs.dump(result)

        return make_response(jsonify(serialized_result), 200)

    @jwt_required()
    def put(self, id):
        fs_bd = formation_service.get_formation_by_id(id)
        if not fs_bd:
            return make_response(jsonify({'error': 'Formation not found'}), 404)
        fs = formation_schema.FormationSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            description = request.json['description']
            teachers = request.json['teachers']

            new_formation = formation_entity.FormationEntity(name=name, description=description, teachers=teachers)
            formation_service.update_formation(fs_bd, new_formation)

            result = formation_service.get_formation_by_id(id)
            serialized_result = fs.dump(result)

            return make_response(jsonify(serialized_result), 200)

    @jwt_required()
    def delete(self, id):
        result = formation_service.get_formation_by_id(id)
        if not result:
            return make_response(jsonify({'error': 'Formation not found'}), 404)
        else:
            formation_service.delete_formation(result)
        fs = formation_schema.FormationSchema()
        serialized_result = fs.dump(result)
        return make_response(jsonify(serialized_result), 200)


api.add_resource(FormationView, '/formation')
api.add_resource(FormationByIdView, '/formation/<int:id>')
