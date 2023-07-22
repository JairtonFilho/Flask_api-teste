from api.models import teacher_model
from api import db


def add_teacher(teacher):
    teacher_bd = teacher_model.TeacherModel(name=teacher.name, age=teacher.age)
    db.session.add(teacher_bd)
    db.session.commit()
    return teacher_bd


def get_teachers():
    return teacher_model.TeacherModel.query.all()


def get_teacher_by_id(id):
    return teacher_model.TeacherModel.query.filter_by(id=id).first()


def update_teacher(old_teacher, new_teacher):
    old_teacher.name = new_teacher.name
    old_teacher.age = new_teacher.age
    db.session.commit()
    return old_teacher


def delete_teacher(teacher):
    db.session.delete(teacher)
    db.session.commit()
