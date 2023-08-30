from api.models import user_model
from api import db


def add_user(user):
    user_bd = user_model.UserModel(name=user.name, email=user.email, password=user.password, is_admin=user.is_admin)
    user_bd.password_encrypt()
    db.session.add(user_bd)
    db.session.commit()
    return user_bd

def get_user_by_email(email):
    return user_model.UserModel.query.filter_by(email=email).first()

def get_user_by_id(id):
    return user_model.UserModel.query.filter_by(id=id).first()