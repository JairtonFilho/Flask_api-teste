from api.models import user_model
from api import db


def add_user(user):
    user_bd = user_model.UserModel(name=user.name, email=user.email, password=user.password)
    user.bd.password_encrypt(user.password)
    db.session.add(user_bd)
    db.session.commit()
    return user_bd
