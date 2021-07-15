import os

BASEDIR = os.getcwd()
APP_DIR = os.getenv("CLOUD_SERVICE_DIR", "/tmp/cloud_service")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config.config import config

db = SQLAlchemy()

def create_app(config_name):

    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db = SQLAlchemy(app)
    db.init_app(app)
    
    from app.route import root, user
    app.register_blueprint(root.root)
    app.register_blueprint(user.user)

    return app