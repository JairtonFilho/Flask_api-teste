from flask_restful import Resource
from api import api
from api.schemas import course_schema
from flask import request, make_response, jsonify
from api.entities import course_entity
from api.services import course_service, formation_service

class CourseView(Resource):
    def get(self):

        cs = course_schema.CourseSchema(many=True)
        result = course_service.get_courses()
        serialized_result = cs.dump(result)

        return make_response(jsonify(serialized_result), 200)

    def post(self):
        cs = course_schema.CourseSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            description = request.json['description']
            publication_date = request.json['publication_date']
            formation = request.json['formation']
            formation_course = formation_service.get_formation_by_id(formation)

            if formation_course is None:
                return make_response(jsonify({'error': 'Formation not found'}), 404)

            new_course = course_entity.CourseEntity(name=name, description=description,
                                                    publication_date=publication_date, formation=formation_course)
            result = course_service.add_course(new_course)
            serialized_result = cs.dump(result)

            return make_response(jsonify(serialized_result), 201)

class CourseByIdView(Resource):
    def get(self, id):
        result = course_service.get_course_by_id(id)
        if not result:
            return make_response(jsonify({'error': 'Course not found'}), 404)
        else:
            cs = course_schema.CourseSchema()

        serialized_result = cs.dump(result)

        return make_response(jsonify(serialized_result), 200)

    def put(self, id):
        cs_bd = course_service.get_course_by_id(id)
        if not cs_bd:
            return make_response(jsonify({'error': 'Course not found'}), 404)
        cs = course_schema.CourseSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            description = request.json['description']
            publication_date = request.json['publication_date']
            formation = request.json['formation']
            formation_course = formation_service.get_formation_by_id(formation)

            if formation_course is None:
                return make_response(jsonify({'error': 'Formation not found'}), 404)

            new_course = course_entity.CourseEntity(name=name, description=description,
                                                    publication_date=publication_date, formation=formation_course)
            course_service.update_course(cs_bd, new_course)

            result = course_service.get_course_by_id(id)
            serialized_result = cs.dump(result)

            return make_response(jsonify(serialized_result), 200)

    def delete(self, id):
        result = course_service.get_course_by_id(id)
        if not result:
            return make_response(jsonify({'error': 'Course not found'}), 404)
        else:
            course_service.delete_course(result)
        cs = course_schema.CourseSchema()
        serialized_result = cs.dump(result)
        return make_response(jsonify(serialized_result), 200)

api.add_resource(CourseView, '/course')
api.add_resource(CourseByIdView, '/course/<int:id>')