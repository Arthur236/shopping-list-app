"""
Class fot shopping list items test cases
"""
import unittest
from app.list_items import ListItems

class TestCasesItems(unittest.TestCase):
    """
    Test cases for shopping list items
    """

    def setUp(self):
        """
        Setting up dataset
        """
        self.list_data = ListItems()

    def tearDown(self):
        """
        Delete dataset
        """
        del self.list_data

    def test_if_item_exists(self):
        """
        Test if list item exists
        """
        self.list_data.item_list = [{'owner': 'random', 'list': 'List 1', 'name': 'Item 1'}, {'owner': 'random', 'list': 'List 2', 'name': 'Item 2'}]
        result = self.list_data.add_item("random", "List 1", "Item 1")
        self.assertEqual(result, "Item already exists")

    def test_for_special_characters(self):
        """
        Test of item name has special characters
        """
        result = self.list_data.add_item("random", "List 1", "Item 1")
        self.assertEqual(result, "Name cannot contain special characters")

    def test_for_item_owner(self):
        """
        Test if item belongs to owner
        """
        self.list_data.item_list = [{'owner': 'random', 'list': 'List 1', 'name': 'Item 1'}, {'owner': 'random2', 'list': 'List 2', 'name': 'Item 1'}]
        result = self.list_data.show_items("random", "List 1")
        self.assertEqual(result, [{'owner': 'random', 'list': 'List 1', 'name': 'Item 1'}])

    def test_item_creation(self):
        """
        Test for correct item creation
        """
        result = self.list_data.add_item("random", "List 1", "Item 1")
        self.assertEqual(result, [{'owner': 'random', 'list': 'List 1', 'name': 'Item 1'}])

    def test_edit_works(self):
        """
        Test if items are editted correctly
        """
        self.list_data.item_list = [{'owner': 'random', 'list': 'List 1', 'name': 'Item 1'}]
        result = self.list_data.edit_item('Item 1', 'Item 2', 'List 1', "random")
        self.assertEqual(result, [{'owner': 'random', 'list': 'List 1', 'name': 'Item 2'}])

    def test_item_exists_on_edit(self):
        """
        Test if name of item exists when trying to edit
        """
        self.list_data.item_list = [{'owner': 'random', 'list': 'List 1', 'name': 'Item 1'}, {'owner': 'random', 'list': 'List 1', 'name': 'Item 2'}]
        result = self.list_data.edit_item('Item 1', 'Item 2', 'List 1', "random")
        self.assertEqual(result, "Item already exists")

    def test_item_delete(self):
        """
        Test if item is deleted successfully
        """
        self.list_data.item_list = [{'owner': 'random', 'list': 'List 1', 'name': 'Item 1'}, {'owner': 'random', 'list': 'List 1', 'name': 'Item 2'}]
        result = self.list_data.delete_item('Item 1', "List 1", 'random')
        self.assertEqual(result, ['Item 2'])

    def test_delete_list_items(self):
        """
        Test if a deleting a list deletes it's items
        """
        self.list_data.item_list = [{'owner': 'random', 'list': 'List 1', 'name': 'Item 1'}, {'owner': 'random', 'list': 'List 1', 'name': 'Item 2'}]
        res = self.list_data.delete_list('List 1')
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()

