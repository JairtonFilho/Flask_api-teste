from flask_restful import Resource
from api import api
from api.schemas import teacher_schema
from flask import request, make_response, jsonify
from api.entities import teacher_entity
from api.services import teacher_service
from api.paginate import paginate
from api.models.teacher_model import TeacherModel
from flask_jwt_extended import jwt_required


class TeacherView(Resource):
    @jwt_required()
    def get(self):
        ts = teacher_schema.TeacherSchema(many=True)
        return paginate(TeacherModel, ts)

    @jwt_required()
    def post(self):
        ts = teacher_schema.TeacherSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            age = request.json['age']

            new_teacher = teacher_entity.TeacherEntity(name=name, age=age)
            result = teacher_service.add_teacher(new_teacher)
            serialized_result = ts.dump(result)

            return make_response(jsonify(serialized_result), 201)


class TeacherByIdView(Resource):
    @jwt_required()
    def get(self, id):
        result = teacher_service.get_teacher_by_id(id)
        if not result:
            return make_response(jsonify({'error': 'Teacher not found'}), 404)
        else:
            ts = teacher_schema.TeacherSchema()

        serialized_result = ts.dump(result)

        return make_response(jsonify(serialized_result), 200)

    @jwt_required()
    def put(self, id):
        ts_bd = teacher_service.get_teacher_by_id(id)
        if not ts_bd:
            return make_response(jsonify({'error': 'Teacher not found'}), 404)
        ts = teacher_schema.TeacherSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            age = request.json['age']

            new_teacher = teacher_entity.TeacherEntity(name=name, age=age)
            teacher_service.update_teacher(ts_bd, new_teacher)

            result = teacher_service.get_teacher_by_id(id)
            serialized_result = ts.dump(result)

            return make_response(jsonify(serialized_result), 200)

    @jwt_required()
    def delete(self, id):
        result = teacher_service.get_teacher_by_id(id)
        if not result:
            return make_response(jsonify({'error': 'Teacher not found'}), 404)
        else:
            teacher_service.delete_teacher(result)
        ts = teacher_schema.TeacherSchema()
        serialized_result = ts.dump(result)
        return make_response(jsonify(serialized_result), 200)


api.add_resource(TeacherView, '/teacher')
api.add_resource(TeacherByIdView, '/teacher/<int:id>')
