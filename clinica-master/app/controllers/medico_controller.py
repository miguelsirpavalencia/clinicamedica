from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from app.models.medico import Medico
from app import db

medico_bp = Blueprint(
    'medico',
    __name__,
    url_prefix='/medicos'
)


# LISTAR
@medico_bp.route('/')
def listar():

    medicos = Medico.query.all()

    return render_template(
        'medicos/listar.html',
        medicos=medicos
    )


# CREAR
@medico_bp.route('/crear', methods=['GET', 'POST'])
def crear():

    if request.method == 'POST':

        medico = Medico(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad'],
            telefono=request.form['telefono'],
            correo=request.form['correo']
        )

        db.session.add(medico)

        db.session.commit()

        return redirect('/medicos/')

    return render_template('medicos/crear.html')


# EDITAR
@medico_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    medico = Medico.query.get_or_404(id)

    if request.method == 'POST':

        medico.nombre = request.form['nombre']
        medico.especialidad = request.form['especialidad']
        medico.telefono = request.form['telefono']
        medico.correo = request.form['correo']

        db.session.commit()

        return redirect('/medicos/')

    return render_template(
        'medicos/editar.html',
        medico=medico
    )


# ELIMINAR
@medico_bp.route('/eliminar/<int:id>')
def eliminar(id):

    medico = Medico.query.get_or_404(id)

    db.session.delete(medico)

    db.session.commit()

    return redirect('/medicos/')