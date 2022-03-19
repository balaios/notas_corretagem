import os

from flask import Flask

from .extensions import db, ma, migrate
from .routes.api import api
from .routes.main import main


def create_app():

    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:postgres@localhost/notas_corretagem"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    UPLOAD_FOLDER = os.path.join(os.getcwd(), "notas_corretagem/uploads/")
    if not os.path.isdir(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)

    db.init_app(app)
    migrate.init_app(app, db)

    ma.init_app(app)

    app.register_blueprint(api)
    app.register_blueprint(main)

    return app
