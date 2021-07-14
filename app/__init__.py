import os
BASEDIR = os.getcwd()
APP_DIR = os.getenv("CLOUD_SERVICE_DIR", "/tmp/cloud_service")

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    from app.route import root, user
    app.register_blueprint(root.root)
    app.register_blueprint(user.user)

    return app