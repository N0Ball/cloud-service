import os
import datetime

from app import BASEDIR

def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(f'{BASEDIR}/tests/', db_name)

class BaseConfig:
    SECRET_KEY = os.environ['SECRET_KEY']
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)

class DevelopmentConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    username = os.environ['MYSQL_USER']
    password = os.environ['MYSQL_PASS']
    database = os.environ['MYSQL_DB']
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{username}:{password}@cloud-service-db:3306/{database}'

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")

config = {
    'DEVELOPMENT': DevelopmentConfig,
    'TESTING': TestingConfig,
}