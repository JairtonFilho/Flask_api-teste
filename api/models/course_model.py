from api import db
from api.models import formation_model


class CourseModel(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.Date, nullable=False)

    formation_id = db.Column(db.Integer, db.ForeignKey("formations.id"))
    formation = db.relationship(formation_model.FormationModel, backref=db.backref("course", lazy="dynamic"))
