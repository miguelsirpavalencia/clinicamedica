from app import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):

    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))