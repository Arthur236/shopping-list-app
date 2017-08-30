"""
Setting up our unit tests
"""
import unittest
from app.users import User

class ShoppingListTests(unittest.TestCase):
    """
    Class to hold test cases
    """

    def setUp(self):
        """
        Setting up User before testing
        """
        self.user = User()

    def tearDown(self):
        """
        Clearing dataset after testing
        """
        del self.user

    def test_if_user_exists(self):
        """
        Test case to check if a user already exists
        """
        self.user.create_user("random", "pass123", "pass123")
        result = self.user.create_user("random", "pass123", "pass123")
        self.assertEqual(result, "The user already exists.")

    if __name__ == '__main__':
        unittest.main()
