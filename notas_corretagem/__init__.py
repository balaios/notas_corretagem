import os

from flask import Flask

from .extensions import db, migrate
from .routes.main import main


def create_app():

    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:postgres@localhost/notas"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    UPLOAD_FOLDER = os.path.join(os.getcwd(), "notas_corretagem/uploads/")
    if not os.path.isdir(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    return app
