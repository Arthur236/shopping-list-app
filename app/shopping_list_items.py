"""
Code for shopping list items
"""
import re

class ListItems(object):
    """
    Contains functions for CRUD operations
    """

    def __init__(self):
        self.list_items = []

    def show_items(self, user, list_name):
        """
        Returns items belonging to a user
            Arguments:
                user: string
                list_name: string
            Returns:
                List of items in a shopping list
        """
        user_items = [item for item in self.list_items if item['owner'] == user and item['list'] == list_name]
        return user_items

    def add_item(self, user, list_name, item_name):
        """
        Add items to a shopping list
            Args
                user: string
                list_name: string
                item_name: string
            result
                list of items
        """
        if re.match("^[a-zA-Z0-9 :_]*$", item_name):
            # Get users items
            users_items = self.show_items(user, list_name)
            for item in users_items:
                if item['name'] == item_name:
                    return "Item already exists"
            activity_dict = {
                'owner': user,
                'list': list_name,
                'name': item_name
            }
            self.list_items.append(activity_dict)
            return self.show_items(user, list_name)
        else:
            return "Name cannot contain special characters"

    def update_item(self, old_name, new_name, list_name, user):
        """
        Edit list items
            Arguments:
                old_name: string
                new_name: string
                list_name: string
                user: string
            Returns:
                Status message
        """
        if re.match("^[a-zA-Z0-9 :_]*$", new_name):
            user_items = self.show_items(user, list_name)

            for item in user_items:
                if item['list'] == list_name:
                    if item['name'] != new_name and item['name'] == old_name:
                        item['name'] = new_name
                    else:
                        return "Item already exists"
            return "Item edited successfully"
        else:
            return "The name cannot contain special characters"

    def delete_item(self, item_name, list_name, user):
        """
        Delete items
            Arguments:
                item_name: string
                list_name: string
                user: string
            Returns:
                List
        """
        # Get users activities
        for item in range(len(self.list_items)):
            if self.list_items[item]['name'] == item_name:
                del self.list_items[item]
                break

        user_items = self.show_items(user, list_name)

        return user_items

    def delete_list_items(self, list_name):
        """
        Delete items for the list that was deleted
            Arguments:
                list_name: string
        """
        for i in range(len(self.list_items)):
            if self.list_items[i]['list'] == list_name:
                del self.list_items[i]
                break
