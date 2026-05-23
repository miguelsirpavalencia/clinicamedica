from app import db
from datetime import datetime

class Cita(db.Model):

    __tablename__ = 'citas'

    id_cita = db.Column(db.Integer, primary_key=True)

    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    motivo = db.Column(db.String(200), nullable=False)

    id_medico = db.Column(
        db.Integer,
        db.ForeignKey('medicos.id_medico'),
        nullable=False
    )

    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey('pacientes.id_paciente'),
        nullable=False
    )