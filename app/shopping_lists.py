"""
Code to handle CRUD operations of shopping lists
"""
import re


class ShoppingList(object):
    """
    Handles CRUD
    """

    def __init__(self):
        self.shopping_list = []

    def show_lists(self, username):
        """
        Returns shopping lists belonging to a user
            Arguments:
                username: string
            Returns:
                A list of a user's shopping lists
        """
        # using list comprehension to make a new list containing only lists belonging to a user
        users_list = [item for item in self.shopping_list if item['owner'] == username]
        return users_list

    def check_list_exists(self, user, list_name):
        """
        Checks whether a list exists or not
        Arguments:
                user: string
                list_name: string
            Returns:
                True or False
        """
        users_lists = self.show_lists(user)
        if not any(d.get('name', None).lower() == list_name.lower() for d in users_lists):
            return False
        return True

    def create_list(self, username, name, description):
        """
        Creating a shopping lists
            Arguments:
                name: string
                username: string
                description: string
            Returns:
                Shopping list
        """
        # Check for special characters
        if not re.match("^[a-zA-Z0-9 _]*$", name):
            return "The name cannot contain special characters"

        # # Get users shopping lists
        # user_lists = self.show_lists(username)
		#
        # # Check if shopping list exists
        # for item in user_lists:
        #     if name.lower() == item['name'].lower():
        #         return "That shopping list already exists."
        item_exists = self.check_list_exists(username, name)
        if item_exists is False:
            shopping_dict = {'owner': username, 'name': name, 'description': description}
            self.shopping_list.append(shopping_dict)
            return self.show_lists(username)

        return "That shopping list already exists."

    def update_list(self, old_name, new_name, description, user):
        """
        Update shopping list name
            Arguments:
                old_name: string
                new_name: string
                description: string
                user: string
            Returns:
            Status message
        """
        if not re.match("^[a-zA-Z0-9 _]*$", new_name):
            return "The name cannot contain special characters"

        users_lists = self.show_lists(user)
        list_exists = self.check_list_exists(user, new_name)

        for item in users_lists:
            if old_name.lower() == new_name.lower() and item['name'].lower() == old_name.lower():
                if list_exists is True:
                    del item['name']
                    del item['description']
                    edit_dict = {'name': new_name, 'description': description}
                    item.update(edit_dict)

            if item['name'].lower() != new_name.lower() and item['name'].lower() == old_name.lower():
                if list_exists is True:
                    return "That name is already in use"

                del item['name']
                del item['description']
                edit_dict = {'name': new_name, 'description': description}
                item.update(edit_dict)

        return self.show_lists(user)

    def delete_list(self, name, user):
        """
        Delete shopping list
            Arguments:
                 name: string
                 user: string
            Returns:
                 New list
        """
        # Delete shopping list
        for item in range(len(self.shopping_list)):
            if self.shopping_list[item]['name'] == name:
                del self.shopping_list[item]
                break

        # Get users shopping list
        users_lists = self.show_lists(user)
        return users_lists
