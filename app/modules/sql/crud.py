from app import db
from . import models

def create_user(name:str, password:str, role: str="default"):
    new_user = models.User(name, password, role)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user_by_id(id: int):
    return models.User.query.filter_by(uid=id).first()

def get_user_by_name(name: str):
    return models.User.query.filter_by(name=name).first()

def get_user_by_role(role: str, start=0, limit=10):
    return models.User.query.filter_by(role=role).offset(start).limit(limit).all()

def update_user_password(user: models.User, password: str):
    user.password = password
    db.session.add(user)
    db.session.commit()
    return user

def update_user_role(user: models.User, role: str):
    user.role = role
    db.session.add(user)
    db.session.commit()
    return user

def del_user(user: models.User):
    user.role = 'del'
    db.session.add(user)
    db.session.commit()
    return user

def create_container(name: str ,port: int):
    new_ct = models.Container(name, port)
    db.session.add(new_ct)
    db.session.commit()
    return new_ct

def get_container_by_id(id: int):
    return models.Container.query.filter_by(cid=id).first()

def get_container_by_name(name: str):
    return models.Container.query.filter_by(name=name).first()

def get_container_by_port(port: int):
    return models.Container.query.filter_by(port=port).first()

def update_container_port(ct: models.Container, port: int):
    ct.port = port
    db.session.add(ct)
    db.session.commit()
    return ct

def start_container(ct: models.Container):
    ct.status = 1
    db.session.add(ct)
    db.session.commit()
    return ct

def stop_container(ct: models.Container):
    ct.status = 2
    db.session.add(ct)
    db.session.commit()
    return ct

def del_container(ct: models.Container):
    ct.status = 0
    db.session.add(ct)
    db.session.commit()
    return ct

def create_own_ct_record(uid: int, cid: int):
    new_record = models.OwnCtRecord(uid, cid)
    db.session.add(new_record)
    db.session.commit()
    return new_record

def get_own_ct_record(uid: int, cid: int):
    return models.OwnCtRecord.query.filter_by(uid=uid, cid=cid).first()

def del_own_ct_record(ct_record: models.OwnCtRecord):
    db.session.delete(ct_record)
    db.session.commit()
    return ct_record
