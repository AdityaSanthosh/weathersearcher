import unittest
from unittest import mock
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):
    def test_hashing(self):
        print("Testing if the hashing is Working correctly..")
        pwd = "test"
        self.assertEqual(type(main.hash_password(pwd)), bytes, "Hashing is not working properly!")

    def test_load_db(self):
        print("Testing if the database is loading..")
        with open('db.pkl', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            self.assertEqual(type(content), str, "Database is Corrupted!")

    def test_newuser(self):
        username = "test"
        pwd = "test"
        newuser = main.User(username, pwd)
        users_list = main.load_db()
        users_list.append(newuser)
        main.save_obj(users_list)
        users_list = main.load_db()
        if "test" in users_list:
            print("OK")
        else:
            print("Test Failed")



if __name__ == '__main__':
    unittest.main()
