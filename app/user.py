import json

from flask import Blueprint, render_template, request
from . import db

user = Blueprint('user', __name__, url_prefix='/user')

@user.get('/add')
def add_user():

    return render_template('user/add.html')

@user.post('/add')
def create_user():

    PORT = db.create_user(request.form['username'], request.form['password'])

    return json.dumps({
        "ssh": f"{PORT}22",
        "apache": f"{PORT}80"
    })