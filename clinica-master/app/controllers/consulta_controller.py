from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import Response

from app.models.consulta import Consulta
from app.models.medico import Medico
from app.models.paciente import Paciente

from app import db

consulta_bp = Blueprint(
    'consulta',
    __name__,
    url_prefix='/consultas'
)


# =========================================
# LISTAR CONSULTAS
# =========================================
@consulta_bp.route('/')
def listar():

    consultas = Consulta.query.all()

    return render_template(
        'consultas/listar.html',
        consultas=consultas
    )


# =========================================
# CREAR CONSULTA
# =========================================
@consulta_bp.route('/crear', methods=['GET', 'POST'])
def crear():

    medicos = Medico.query.all()

    pacientes = Paciente.query.all()

    if request.method == 'POST':

        consulta = Consulta(

            fecha=request.form['fecha'],

            diagnostico=request.form['diagnostico'],

            tratamiento=request.form['tratamiento'],

            id_medico=request.form['id_medico'],

            id_paciente=request.form['id_paciente']

        )

        db.session.add(consulta)

        db.session.commit()

        return redirect('/consultas/')

    return render_template(
        'consultas/crear.html',
        medicos=medicos,
        pacientes=pacientes
    )


# =========================================
# EDITAR CONSULTA
# =========================================
@consulta_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    consulta = Consulta.query.get_or_404(id)

    medicos = Medico.query.all()

    pacientes = Paciente.query.all()

    if request.method == 'POST':

        consulta.fecha = request.form['fecha']

        consulta.diagnostico = request.form['diagnostico']

        consulta.tratamiento = request.form['tratamiento']

        consulta.id_medico = request.form['id_medico']

        consulta.id_paciente = request.form['id_paciente']

        db.session.commit()

        return redirect('/consultas/')

    return render_template(
        'consultas/editar.html',
        consulta=consulta,
        medicos=medicos,
        pacientes=pacientes
    )


# =========================================
# ELIMINAR CONSULTA
# =========================================
@consulta_bp.route('/eliminar/<int:id>')
def eliminar(id):

    consulta = Consulta.query.get_or_404(id)

    db.session.delete(consulta)

    db.session.commit()

    return redirect('/consultas/')


# =========================================
# FILTRAR CONSULTAS POR FECHA
# =========================================
@consulta_bp.route('/buscar')
def buscar():

    fecha = request.args.get('fecha')

    consultas = Consulta.query.filter_by(
        fecha=fecha
    ).all()

    return render_template(
        'consultas/listar.html',
        consultas=consultas
    )


# =========================================
# HISTORIAL MEDICO
# =========================================
@consulta_bp.route('/historial/<int:id_paciente>')
def historial(id_paciente):

    paciente = Paciente.query.get_or_404(
        id_paciente
    )

    consultas = Consulta.query.filter_by(
        id_paciente=id_paciente
    ).all()

    return render_template(
        'consultas/historial.html',
        consultas=consultas,
        paciente=paciente
    )


# =========================================
# EXPORTAR REPORTE CSV
# =========================================
@consulta_bp.route('/reporte')
def reporte():

    consultas = Consulta.query.all()

    def generar():

        encabezado = [
            'ID',
            'Fecha',
            'Paciente',
            'Medico',
            'Diagnostico',
            'Tratamiento'
        ]

        yield ','.join(encabezado) + '\n'

        for c in consultas:

            fila = [

                str(c.id_consulta),

                str(c.fecha),

                c.paciente.nombre,

                c.medico.nombre,

                c.diagnostico,

                c.tratamiento

            ]

            yield ','.join(fila) + '\n'

    return Response(
        generar(),
        mimetype='text/csv',
        headers={
            'Content-Disposition':
            'attachment; filename=reporte_consultas.csv'
        }
    )