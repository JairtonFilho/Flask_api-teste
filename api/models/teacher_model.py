from api import db



class TeacherModel(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    formations = db.relationship('FormationModel', secondary='teachers_formations', back_populates='teachers')
