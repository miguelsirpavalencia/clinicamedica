from flask import Blueprint
from flask import render_template

from app.models.medico import Medico
from app.models.paciente import Paciente
from app.models.consulta import Consulta

admin_bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/dashboard'
)

@admin_bp.route('/')
def dashboard():

    total_medicos = Medico.query.count()
    total_pacientes = Paciente.query.count()
    total_consultas = Consulta.query.count()

    return render_template(
        'dashboard.html',
        total_medicos=total_medicos,
        total_pacientes=total_pacientes,
        total_consultas=total_consultas
    )