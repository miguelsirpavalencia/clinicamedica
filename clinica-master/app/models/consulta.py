from app import db
from datetime import datetime

class Consulta(db.Model):

    __tablename__ = 'consultas'

    id_consulta = db.Column(db.Integer, primary_key=True)

    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    diagnostico = db.Column(db.Text, nullable=False)
    tratamiento = db.Column(db.Text, nullable=False)

    id_medico = db.Column(
        db.Integer,
        db.ForeignKey('medicos.id_medico')
    )

    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey('pacientes.id_paciente')
    )