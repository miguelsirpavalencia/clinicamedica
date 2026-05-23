from flask import Blueprint, render_template
from flask import request, redirect

from app.models.paciente import Paciente
from app.models.consulta import Consulta
from app import db

paciente_bp = Blueprint(
    'paciente',
    __name__,
    url_prefix='/pacientes'
)

# LISTAR
@paciente_bp.route('/')
def listar():

    pacientes = Paciente.query.all()

    return render_template(
        'pacientes/listar.html',
        pacientes=pacientes
    )

# CREAR
@paciente_bp.route('/crear', methods=['GET', 'POST'])
def crear():

    if request.method == 'POST':

        paciente = Paciente(
            nombre=request.form['nombre'],
            edad=request.form['edad'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono']
        )

        db.session.add(paciente)
        db.session.commit()

        return redirect('/pacientes')

    return render_template('pacientes/crear.html')

# EDITAR
@paciente_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    paciente = Paciente.query.get_or_404(id)

    if request.method == 'POST':

        paciente.nombre = request.form['nombre']
        paciente.edad = request.form['edad']
        paciente.direccion = request.form['direccion']
        paciente.telefono = request.form['telefono']

        db.session.commit()

        return redirect('/pacientes')

    return render_template(
        'pacientes/editar.html',
        paciente=paciente
    )

# ELIMINAR
@paciente_bp.route('/eliminar/<int:id>')
def eliminar(id):

    paciente = Paciente.query.get_or_404(id)

    db.session.delete(paciente)
    db.session.commit()

    return redirect('/pacientes')

# HISTORIAL MEDICO
@paciente_bp.route('/historial/<int:id>')
def historial(id):

    paciente = Paciente.query.get_or_404(id)

    consultas = Consulta.query.filter_by(
        id_paciente=id
    ).all()

    return render_template(
        'pacientes/historial.html',
        paciente=paciente,
        consultas=consultas
    )