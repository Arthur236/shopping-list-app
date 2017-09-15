"""
Class fot shopping list items test cases
"""
import unittest
from app.shopping_list_items import ListItems

class TestCasesItems(unittest.TestCase):
    """
    Test cases for shopping list items
    """

    def setUp(self):
        """
        Setting up dataset
        """
        self.list_data = ListItems()
        self.list_data.list_items = [{'owner': 'random', 'list': 'List 1',
                                      'name': 'Item 1', 'quantity': '2', 'price': '200'},
                                     {'owner': 'random', 'list': 'List 1', 'name': 'Item 2',
                                      'quantity': '2', 'price': '400'}]

    def tearDown(self):
        """
        Delete dataset
        """
        del self.list_data

    def test_if_item_exists(self):
        """
        Test if list item exists
        """
        result = self.list_data.add_item("random", "List 1", "Item 1", "2", "200")
        self.assertEqual(result, "Item already exists")

    def test_for_special_characters(self):
        """
        Test of item name has special characters
        """
        result = self.list_data.add_item("random", "List 1", "Item 1/*", '2', '200')
        self.assertEqual(result, "Name cannot contain special characters")

    def test_for_item_owner(self):
        """
        Test if item belongs to owner
        """
        result = self.list_data.show_items("random", "List 1")
        self.assertEqual(result, [{'owner': 'random', 'list': 'List 1',
                                   'name': 'Item 1', 'quantity': '2', 'price': '200'},
                                  {'owner': 'random', 'list': 'List 1', 'name': 'Item 2',
                                   'quantity': '2', 'price': '400'}])

    def test_item_creation(self):
        """
        Test for correct item creation
        """
        result = self.list_data.add_item("random", "List 1", "Item 4", '2', '200')
        self.assertEqual(result, [{'owner': 'random', 'list': 'List 1',
                                   'name': 'Item 1', 'quantity': '2', 'price': '200'},
                                  {'owner': 'random', 'list': 'List 1', 'name': 'Item 2',
                                   'quantity': '2', 'price': '400'},
                                  {'owner': 'random', 'list': 'List 1', 'name': 'Item 4',
                                   'quantity': '2', 'price': '200'}])

    def test_edit_works(self):
        """
        Test if items are edited correctly
        """
        result = self.list_data.update_item('Item 1', 'Item 3', 'List 1', 'random', '2', '200')
        self.assertEqual(result, "Item edited successfully")

    def test_item_exists_on_edit(self):
        """
        Test if name of item exists when trying to edit
        """
        result = self.list_data.update_item('Item 2', 'Item 1', 'List 1', 'random', '2', '200')
        self.assertEqual(result, "Item already exists")

    def test_item_delete(self):
        """
        Test if item is deleted successfully
        """
        result = self.list_data.delete_item('Item 1', "List 1", 'random')
        self.assertEqual(result, [{'owner': 'random', 'list': 'List 1',
                                   'name': 'Item 2', 'quantity': '2', 'price': '400'}])

    def test_delete_list_items(self):
        """
        Test if a deleting a list deletes it's items
        """
        res = self.list_data.delete_list_items('List 1')
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
