import unittest
import login
from unittest.mock import Mock, patch


class TestLogin(unittest.TestCase):
    def test_login(self):
        self.assertFalse(login.login().logged_in)


if __name__ == '__main__':
    unittest.main()
