from api.models import formation_model
from api import db
from api.services.teacher_service import get_teacher_by_id
from flask import jsonify


def add_formation(formation):
    formation_bd = formation_model.FormationModel(name=formation.name, description=formation.description)
    for i in formation.teachers:
        teacher = get_teacher_by_id(i)

        formation_bd.teachers.append(jsonify(teacher))
    db.session.add(formation_bd)
    db.session.commit()
    return formation_bd

def get_formations():
    return formation_model.FormationModel.query.all()

def get_formation_by_id(id):
    return formation_model.FormationModel.query.filter_by(id=id).first()

def update_formation(old_formation, new_formation):
    old_formation.name = new_formation.name
    old_formation.description = new_formation.description
    for i in new_formation.teachers:
        teacher = get_teacher_by_id(i)
        old_formation.teachers.append(teacher)
    db.session.commit()
    return old_formation

def delete_formation(formation):
    db.session.delete(formation)
    db.session.commit()
