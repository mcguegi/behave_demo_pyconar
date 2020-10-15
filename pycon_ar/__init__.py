from flask import Flask
from extensions import db
from .routes import pycon_ar


def create_app(config_file="settings.py"):
    app = Flask(__name__, template_folder='templates')

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(pycon_ar)

    return app
