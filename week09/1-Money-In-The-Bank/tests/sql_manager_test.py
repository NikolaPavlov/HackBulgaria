import sys
import unittest

sys.path.append("..")

import sql_manager
from sql_manager import *


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', 'StrongPassFuckJ0hnTheR1pper#', 'fuckmf@wearefucked.com')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', 'StrongPassFuckJ0hnTheR1pper#', 'fuckmf@wearefucked.com')

        sql_manager.cursor.execute('''
            SELECT Count(*) FROM clients
            WHERE username = (?) AND password = (?)''',
            ('Dinko', hash_pass('StrongPassFuckJ0hnTheR1pper#')))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', "StrongPassFuckJ0hnTheR1pper#")
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_sql_injections_fails(self):
        logged_user = sql_manager.login("' OR 1 = 1 --", 'password')
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567A^')
        self.assertFalse(logged_user)

    def test_password_hashed(self):
        sql_manager.login('Tester', "StrongPassFuckJ0hnTheR1pper#")
        sql_manager.cursor.execute('''
            SELECT password FROM clients
            WHERE username = ? AND password = ?
            ''', ('Tester', "StrongPassFuckJ0hnTheR1pper#"))
        password = sql_manager.cursor.fetchone()
        self.assertFalse(password)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', "StrongPassFuckJ0hnTheR1pper#")
        new_message = "kali for the win"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', "StrongPassFuckJ0hnTheR1pper#")
        new_password = "gogo_be_pro_ha7er#"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
