from api import db
from api.models import teacher_model


teacher_formation = db.Table('teachers_formations',
                             db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id'), primary_key=True,
                                       nullable=False),
                             db.Column('formation_id', db.Integer, db.ForeignKey('formations.id'), primary_key=True,
                                       nullable=False))
class FormationModel(db.Model):
    __tablename__ = 'formations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    teachers = db.relationship(teacher_model.TeacherModel, secondary='teachers_formations', back_populates='formations')
