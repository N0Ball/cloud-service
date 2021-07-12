from flask import Blueprint

bp = Blueprint('root', __name__)

@bp.route('/')
def root():
    return "<h1>It works</h1>"