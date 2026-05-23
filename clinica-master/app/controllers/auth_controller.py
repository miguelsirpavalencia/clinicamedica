from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from flask_login import login_user
from flask_login import logout_user

from app.models.usuario import Usuario
from app import db

auth_bp = Blueprint(
    'auth',
    __name__
)

# LOGIN
@auth_bp.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        usuario = Usuario.query.filter_by(
            username=username,
            password=password
        ).first()

        if usuario:

            login_user(usuario)

            # REDIRECCION CORREGIDA
            return redirect('/medicos/')

    return render_template('login.html')


# REGISTER
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        usuario = Usuario(
            username=request.form['username'],
            password=request.form['password']
        )

        db.session.add(usuario)
        db.session.commit()

        return redirect('/')

    return render_template('register.html')


# LOGOUT
@auth_bp.route('/logout')
def logout():

    logout_user()

    return redirect('/')