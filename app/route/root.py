from flask import Blueprint

root = Blueprint('root', __name__)

@root.route('/')
def greets():
    return "<h1>It works</h1>"