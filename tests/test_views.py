"""
Test cases for views.py
"""
from app import app
from app import views
import unittest


class ViewsTest(unittest.TestCase):
	"""
	Class to hold all the tests
	"""

	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		pass

	def test_index_response(self):
		"""
		Test get response of index page
		"""
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)

	def test_dashboard_response(self):
		"""
		Test get response of dashboard page
		"""
		response = self.app.get('/dashboard')
		self.assertEqual(response.status_code, 200)

	def test_create_list_response(self):
		"""
		Test get response of create list page
		"""
		response = self.app.get('/create_list')
		self.assertEqual(response.status_code, 200)

	def test_view_list_response(self):
		"""
		Test get response of view list page
		"""
		response = self.app.get('/view_list/list1')
		self.assertEqual(response.status_code, 200)

	def test_edit_list_response(self):
		"""
		Test get response of edit list page
		"""
		response = self.app.get('/edit_list/list1')
		self.assertEqual(response.status_code, 200)

	def test_edit_item_response(self):
		"""
		Test get response of edit item page
		"""
		response = self.app.get('/edit_item/list1/item1')
		self.assertEqual(response.status_code, 200)

	if __name__ == '__main__':
		unittest.main()
