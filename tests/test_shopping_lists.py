"""
Test class for shopping_lists.py
"""
import unittest
from app.shopping_lists import ShoppingList


class ShoppingListTests(unittest.TestCase):
    """
    Test cases for shopping lists
    """

    def setUp(self):
        """
        Setting up ShoppingList dataset
        """
        self.shopping_list_data = ShoppingList()

    def tearDown(self):
        """
        Delete ShoppingList dataset
        """
        del self.shopping_list_data

    def test_if_shopping_list_exists(self):
        """
        Test if a shopping list exists or not
        """
        self.shopping_list_data.shopping_list = [{'owner': 'random', 'name': 'List 1'}, {'owner': 'random', 'name': 'List 2'}, {'owner': 'random2', 'name': 'List 3'}]
        result = self.shopping_list_data.create_list("random", "List 1", "Brief description")
        self.assertEqual(result, "That shopping list already exists.")

    def test_for_special_characters(self):
        """
        Test if the shopping list has special characters
        """
        result = self.shopping_list_data.create_list("random", "List 1/--*", "Brief description")
        self.assertEqual(result, "The name cannot contain special characters")

    def test_if_list_is_users(self):
        """
        Test if user gets only their lists
        """
        self.shopping_list_data.shopping_list = [{'owner': 'random', 'name': 'List 1'}, {'owner': 'random', 'name': 'List 2'}, {'owner': 'random2','name': 'List 3'}, {'owner': 'random2','name': 'List 4'}, {'owner': 'random2','name': 'List 5'}, {'owner': 'random3', 'name': 'List 6'}]
        result = self.shopping_list_data.show_lists("random2")
        self.assertEqual(result, [{'owner': 'random2', 'name': 'List 3'}, {'owner': 'random2', 'name': 'List 4'}, {'owner': 'random2', 'name': 'List 5'}])

    def test_list_creation(self):
        """
        Test shopping list is correctly created
        """
        result = self.shopping_list_data.create_list("random", "Awesome List", "Brief description")
        self.assertEqual(result, [{'owner': 'random', 'name': 'Awesome List'}])

    def test_shopping_list_update(self):
        """
        Test if list is correctly updated
        """
        self.shopping_list_data.shopping_list = [{'owner': 'random', 'name': 'Awesome List'}]
        result = self.shopping_list_data.update_list('Awesome List', 'Awesome List 2', "Brief description", "random")
        self.assertEqual(result, [{'owner': 'random', 'name': 'Awesome List 2'}])

    def test_update_existing_list(self):
        """
        Test if a list with a similar name is updated or name
        """
        self.shopping_list_data.shopping_list = [{'owner': 'random', 'name': 'List 1'}, {
            'owner': 'random', 'name': 'List 2'}]
        result = self.shopping_list_data.update_list('List 1', 'List 2', "Brief description", "random")
        self.assertEqual(result, "That name is already in use")

    def test_delete_list(self):
        """
        Test if a shopping list is properly deleted
        """
        self.shopping_list_data.shopping_list = [{'owner': 'user1', 'name': 'List 1'}, {'owner': 'user1', 'name': 'List 2'}, {'owner': 'user1', 'name': 'List 3'}]
        result = self.shopping_list_data.delete_list('List 3', "user1")
        self.assertEqual(result, [{'owner': 'user1', 'name': 'List 1'}, {'owner': 'user1', 'name': 'List 2'}])


if __name__ == '__main__':
    unittest.main()
