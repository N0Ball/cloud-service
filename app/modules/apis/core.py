import json

from app.modules.database import db

def create_user(name, password):

    PORT = db.create_user(name, password)

    return json.dumps({
        "ssh": f"1{PORT}",
        "apache": f"2{PORT}"
    })