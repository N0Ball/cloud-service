from datetime import datetime

from flask_testing import TestCase

from app import create_app, db
from app.modules.sql import models

class SettingBase(TestCase):

    def create_app(self):
        return create_app("TESTING")

    def setUp(self):
        db.create_all()
        self.username = "testUser"
        self.passwords = "test_pass"
        self.role = 'admin'

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_default_db(self):
        db.drop_all()
        db.create_all()

        sql = f"""
            INSERT INTO user
            (name, password, role, insert_time, update_time)
            VALUES 
            ('default_user', 'default_pass', 'default', '{datetime.now()}', '{datetime.now()}'),
            ('id_2_user', 'default_pass', 'default', '{datetime.now()}', '{datetime.now()}'),
            ('pro_user', 'pro_pass', 'pro', '{datetime.now()}', '{datetime.now()}'),
            ('admin_user', 'admin_pass', 'admin', '{datetime.now()}', '{datetime.now()}'),
            ('id_5_user', 'admin_pass', 'pro', '{datetime.now()}', '{datetime.now()}'),
            ('del_user1', 'del_pass', 'del', '{datetime.now()}', '{datetime.now()}'),
            ('del_user2', 'del_pass', 'del', '{datetime.now()}', '{datetime.now()}'),
            ('ct1_owner', 'co_pass', 'default', '{datetime.now()}', '{datetime.now()}'),
            ('ct2_owner', 'co_pass', 'admin', '{datetime.now()}', '{datetime.now()}');
        """
        db.engine.execute(sql)

        sql = f"""
            INSERT INTO container
            (name, port, status, insert_time, update_time)
            VALUES 
            ('id_1_ct', 1111, 1, '{datetime.now()}', '{datetime.now()}'),
            ('running_ct', 1000, 1, '{datetime.now()}', '{datetime.now()}'),
            ('del_ct', 404, 0, '{datetime.now()}', '{datetime.now()}'),
            ('id_4_ct', 444, 0, '{datetime.now()}', '{datetime.now()}'),
            ('stop_ct', 301, 2, '{datetime.now()}', '{datetime.now()}'),
            ('port_ct', 666, 2, '{datetime.now()}', '{datetime.now()}'),
            ('ct1', 1001, 1, '{datetime.now()}', '{datetime.now()}'),
            ('ct2', 1002, 2, '{datetime.now()}', '{datetime.now()}');
        """
        db.engine.execute(sql)

        sql = f"""
            INSERT INTO own_ct_record
            (uid, cid, insert_time, update_time)
            VALUES 
            (2, 1, '{datetime.now()}', '{datetime.now()}'),
            (5, 4, '{datetime.now()}', '{datetime.now()}'),
            (5, 3, '{datetime.now()}', '{datetime.now()}'),
            (6, 5, '{datetime.now()}', '{datetime.now()}');
        """
        db.engine.execute(sql)