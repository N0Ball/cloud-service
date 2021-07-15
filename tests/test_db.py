import unittest

from test_factory import SettingBase

from app import db
from app.modules.sql import crud

class CheckUserCrud(SettingBase):

    def test_create_user(self):
        result = crud.create_user("new_user", "ouo")
        self.assertEqual(str(result), 'User(new_user, default)')
        sql = """SELECT name, role FROM user WHERE uid = 1"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [('new_user', 'default')])

    def test_get_default_user_by_id(self):
        self.create_default_db()
        result = crud.get_user_by_id(2)
        self.assertEqual(str(result), 'User(id_2_user, default)')

    def test_get_admin_user_by_name(self):
        self.create_default_db()
        result = crud.get_user_by_name('admin_user')
        self.assertEqual(str(result), 'User(admin_user, admin)')

    def test_get_del_user_by_role(self):
        self.create_default_db()
        result = crud.get_user_by_role('del')
        self.assertEqual(str(result), '[User(del_user1, del), User(del_user2, del)]')

    def test_update_admin_password(self):
        self.create_default_db()
        crud.update_user_password(crud.get_user_by_name('admin_user'), 'new_pass')
        sql = """SELECT name, password FROM user WHERE name = 'admin_user'"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [('admin_user', 'new_pass')])

    def test_update_role(self):
        self.create_default_db()
        crud.update_user_role(crud.get_user_by_name('default_user'), 'admin')
        sql = """SELECT name, password FROM user WHERE role = 'admin'"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [
            ('default_user', 'default_pass'),
            ('admin_user', 'admin_pass'),
            ('ct2_owner', 'co_pass')])

    def test_del_user(self):
        self.create_default_db()
        crud.del_user(crud.get_user_by_name('pro_user'))
        sql = """SELECT name, password FROM user WHERE role = 'del'"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [
            ('pro_user', 'pro_pass'), 
            ('del_user1', 'del_pass'), 
            ('del_user2', 'del_pass')])

class CheckContainerCrud(SettingBase):

    def test_create_container(self):
        crud.create_container("new_ct", 3000)
        sql = """SELECT name, port FROM container"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [('new_ct', 3000)])

    def test_get_container_by_id(self):
        self.create_default_db()
        result = crud.get_container_by_id(1)
        self.assertEqual(str(result), 'Container(id_1_ct, 1111, 1)')

    def test_get_container_by_name(self):
        self.create_default_db()
        result = crud.get_container_by_name('ct1')
        self.assertEqual(str(result), 'Container(ct1, 1001, 1)')

    def test_get_container_by_port(self):
        self.create_default_db()
        result = crud.get_container_by_port(666)
        self.assertEqual(str(result), 'Container(port_ct, 666, 2)')

    def test_update_container_port(self):
        self.create_default_db()
        result = crud.update_container_port(crud.get_container_by_name('ct1'), 10)
        self.assertEqual(str(result), 'Container(ct1, 10, 1)')
        sql = """SELECT name, port FROM container WHERE port = 10"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [('ct1', 10)])

    def test_start_container(self):
        self.create_default_db()
        result = crud.start_container(crud.get_container_by_name('stop_ct'))
        self.assertEqual(str(result), 'Container(stop_ct, 301, 1)')
        sql = """SELECT name, port FROM container WHERE status = 1"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [('id_1_ct', 1111), ('running_ct', 1000), ('stop_ct', 301), ('ct1', 1001)])

    def test_stop_container(self):
        self.create_default_db()
        result = crud.stop_container(crud.get_container_by_name('running_ct'))
        self.assertEqual(str(result), 'Container(running_ct, 1000, 2)')
        sql = """SELECT name, port FROM container WHERE status = 2"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [('running_ct', 1000), ('stop_ct', 301), ('port_ct', 666), ('ct2', 1002)])


    def test_del_container(self):
        self.create_default_db()
        result = crud.del_container(crud.get_container_by_name('stop_ct'))
        self.assertEqual(str(result), 'Container(stop_ct, 301, 0)')
        sql = """SELECT name, port FROM container WHERE status = 0"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [('del_ct', 404), ('id_4_ct', 444), ('stop_ct', 301)])

class CheckOwnCtRecordCrud(SettingBase):

    def test_create_own_ct_record(self):
        self.create_default_db()
        result = crud.create_own_ct_record(3, 1)
        self.assertEqual(str(result), 'OwnCtRecord(3, 1)')
        sql = """SELECT uid, cid FROM own_ct_record WHERE uid = 3 and cid = 1"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [(3, 1)])

    def test_get_own_ct_record(self):
        self.create_default_db()
        crud.get_own_ct_record(2, 1)
        sql = """SELECT uid, cid FROM own_ct_record WHERE uid = 2 and cid = 1"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [(2, 1)])

    def test_del_own_ct_record(self):
        self.create_default_db()
        crud.del_own_ct_record(crud.get_own_ct_record(5, 4))
        sql = """SELECT uid, cid FROM own_ct_record WHERE uid = 5"""
        self.assertEqual(db.engine.execute(sql).fetchall(), [(5, 3)])

if __name__ == '__main__':
    unittest.main()