"""
Test class for users.py
"""
import unittest
from app.users import UserOps

class UserTests(unittest.TestCase):
    """
    Class to hold test cases
    Test if user exists
    Test if passwords match
    Test if password is long enough
    Test if password is wrong
    Test if correct credentials are provided
    """

    def setUp(self):
        """
        Setting up User before testing
        """
        self.user = UserOps()

    def tearDown(self):
        """
        Clearing dataset after testing
        """
        del self.user

    def test_if_user_exists(self):
        """
        Test if a user already exists
        """
        self.user.user_list = [{'username': 'random', 'password': 'pass123'}]
        result = self.user.register("random", "pass123", "pass123")
        self.assertEqual(result, "The user already exists.")

    def test_if_pwds_match(self):
        """
        Test if password matches confirm password
        """
        result = self.user.register("random", "pass123", "pass1234")
        self.assertEqual(result, "The passwords do not match")

    def test_pwd_length(self):
        """
        Test if password is long enough
        """
        result = self.user.register("random", "pass", "pass")
        self.assertEqual(result, "The password should be at least 6 characters long")

    def test_special_chars_in_username(self):
        """
        Test to see if a username has special characters except underscores
        """
        result = self.user.register("random*.+5", "pass123", "pass123")
        self.assertEqual(result, "The username cannot contain special characters. Only underscores")

    def test_if_user_can_register(self):
        """
        Test if the user can register if correct credentials are given
        """
        result = self.user.register("random", "pass123", "pass123")
        self.assertEqual(result, "Registered successfully")

    def test_if_pwd_is_wrong(self):
        """
        Test if wrong password can be detected
        """
        self.user.user_list = [{'username': 'random', 'password': 'pass123'}]
        result = self.user.login("random", "pass1234")
        self.assertEqual(result, "The passwords do not match")

    def test_if_user_does_not_exist(self):
        """
        Test if user exists
        """
        self.user.user_list = [{'username': 'random', 'password': 'pass123'}]
        result = self.user.login("random2", "pass1234")
        self.assertEqual(result, "The user does not exist")

    def test_if_user_can_login(self):
        """
        Test if login works
        """
        self.user.user_list = [{'username': 'random', 'password': 'pass123'}]
        result = self.user.login("random", "pass123")
        self.assertEqual(result, "Login successful")

    if __name__ == '__main__':
        unittest.main()
