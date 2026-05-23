from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

# Inicializar extensiones
db = SQLAlchemy()
login_manager = LoginManager()

# Configuración Flask-Login
login_manager.login_view = 'auth.login'


# Crear aplicación
def create_app():

    app = Flask(__name__)

    # Configuración
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # IMPORTAR MODELO AQUÍ
    from app.models.usuario import Usuario

    # USER LOADER
    @login_manager.user_loader
    def load_user(user_id):

        return Usuario.query.get(int(user_id))

    # Importar Blueprints
    from app.controllers.medico_controller import medico_bp
    from app.controllers.paciente_controller import paciente_bp
    from app.controllers.consulta_controller import consulta_bp
    from app.controllers.auth_controller import auth_bp

    # Registrar Blueprints
    app.register_blueprint(medico_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(consulta_bp)
    app.register_blueprint(auth_bp)

    return app