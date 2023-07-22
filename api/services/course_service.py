from api.models import course_model
from api import db

def add_course(course):
    course_bd = course_model.CourseModel(name=course.name, description=course.description,
                                         publication_date=course.publication_date, formation=course.formation)
    db.session.add(course_bd)
    db.session.commit()
    return course_bd

def get_courses():
    return course_model.CourseModel.query.all()

def get_course_by_id(id):
    return course_model.CourseModel.query.filter_by(id=id).first()

def update_course(old_course, new_course):
    old_course.name = new_course.name
    old_course.description = new_course.description
    old_course.publication_date = new_course.publication_date
    old_course.formation = new_course.formation
    db.session.commit()
    return old_course

def delete_course(course):
    db.session.delete(course)
    db.session.commit()
