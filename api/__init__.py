from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)

from api.views import course_view, formation_view, teacher_view
from api.models import course_model, formation_model, teacher_model
