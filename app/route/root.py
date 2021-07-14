from flask import Blueprint, render_template, url_for

root = Blueprint('root', __name__)

@root.route('/')
def greets():
    return render_template('index.html')

@root.route('/login')
def login():
    return "Login Page"

@root.route('/add')
def add_user():
    return "Add User"

@root.route('/grant')
def grant_privilege():
    return "Grant privilege"