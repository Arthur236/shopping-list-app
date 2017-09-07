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
        if re.match("^[a-zA-Z0-9 _]*$", name):
            # Get users shopping lists
            user_lists = self.show_lists(username)

            # Check if shopping list exists
            for item in user_lists:
                if name.lower() == item['name'].lower():
                    return "That shopping list already exists."
            shopping_dict = {'owner': username, 'name': name, 'description': description}
            self.shopping_list.append(shopping_dict)
            return self.show_lists(username)

        return "The name cannot contain special characters"

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
        if re.match("^[a-zA-Z0-9 _]*$", new_name):
            users_lists = self.show_lists(user)

            for item in users_lists:
                if item['name'].lower() != new_name.lower():
                    if item['name'].lower() == old_name.lower():
                        del item['name']
                        del item['description']
                        edit_dict = {'name': new_name, 'description': description}
                        item.update(edit_dict)
                else:
                    return "That name is already in use"
        else:
            return "The name cannot contain special characters"
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
    