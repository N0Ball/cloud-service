from datetime import datetime

from app import db

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(30), unique=True, comment="currently unused")
    role = db.Column(db.String(10), nullable=False, comment="del for deleted users")
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    containers = db.relationship("OwnCtRecord", backref="user")

    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User({self.name}, {self.role})"

class Container(db.Model):
    __tablename__ = 'container'
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    port = db.Column(db.Integer, unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1, comment="0: deleted, 1: running, 2: closed")
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    owners = db.relationship("OwnCtRecord", backref="container") 

    def __init__(self, name, port):
        self.name = name
        self.port = port

    def __repr__(self):
        return f"Container({self.name}, {self.port}, {self.status})"

class OwnCtRecord(db.Model):
    __tablename__ = 'own_ct_record'
    id = db.Column(db.Integer, primary_key=True)
    insert_time = db.Column(db.DateTime, default=datetime.now, nullable=False)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)

    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    cid = db.Column(db.Integer, db.ForeignKey('container.cid'), nullable=False)

    def __init__(self, uid, cid):
        self.uid = uid
        self.cid = cid

    def __repr__(self):
        return f"OwnCtRecord({self.uid}, {self.cid})"
