import json

from flask import Blueprint, render_template, request

from app.modules.apis import core

user = Blueprint('user', __name__, url_prefix='/user')

@user.get('/add')
def add_user_gui():

    return render_template('user/add.html')

@user.post('/add')
def add_user():

    return core.create_user(request.form['username'], request.form['password'])