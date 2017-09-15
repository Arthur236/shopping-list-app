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
        user_items = \
            [item for item in self.list_items if item['owner'] == user and item['list'] == list_name]
        return user_items

    def check_item_exists(self, user, list_name, item_name):
        """
        Checks whether an item exists or not
        Arguments:
                user: string
                list_name: string
                item_name: string
            Returns:
                True or False
        """
        users_items = self.show_items(user, list_name)
        if not any(d.get('name', None).lower() == item_name.lower() for d in users_items):
            return False
        return True

    def add_item(self, user, list_name, item_name, quantity, price):
        """
        Add items to a shopping list
            Args
                user: string
                list_name: string
                item_name: string
            result
                list of items
        """
        if not re.match("^[a-zA-Z0-9 :_]*$", item_name):
            return "Name cannot contain special characters"

        if not quantity.isnumeric():
            return "Quantity should be an integer"

        if not price.isdigit() or not price.isdecimal():
            return "Price should be a number greater than 0"

        item_exists = self.check_item_exists(user, list_name, item_name)
        if item_exists is False:
            activity_dict = {
                'owner': user,
                'list': list_name,
                'name': item_name,
                'quantity': quantity,
                'price': price
            }
            self.list_items.append(activity_dict)
            return self.show_items(user, list_name)

        return "Item already exists"

    def update_item(self, old_name, new_name, list_name, user, quantity, price):
        """
        Edit list items
            Arguments:
                old_name: string
                new_name: string
                list_name: string
                user: string
                quantity: int
                price: int
            Returns:
                Status message
        """
        if not re.match("^[a-zA-Z0-9 :_]*$", new_name):
            return "The name cannot contain special characters"

        if not quantity.isnumeric():
            return "Quantity should be an integer"

        if not price.isdigit() or not price.isdecimal():
            return "Price should be a number greater than 0"

        user_items = self.show_items(user, list_name)
        item_exists = self.check_item_exists(user, list_name, new_name)

        for item in user_items:
            if item['list'] == list_name:
                if old_name.lower() == new_name.lower() and item['name'].lower() == old_name.lower():
                    if item_exists is True:
                        del item['name']
                        del item['quantity']
                        del item['price']
                        update_dict = {'name': new_name, 'quantity': quantity, 'price': price}
                        item.update(update_dict)
                        return "Item edited successfully"

                if item['name'].lower() != new_name.lower() and item['name'].lower() == old_name.lower():
                    if item_exists is True:
                        return "Item already exists"
                    del item['name']
                    del item['quantity']
                    del item['price']
                    update_dict = {'name': new_name, 'quantity': quantity, 'price': price}
                    item.update(update_dict)
                    return "Item edited successfully"

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
        # Iterate the list in reverse order
        for i in range(len(self.list_items) - 1, -1, -1):
            if self.list_items[i]['list'] == list_name:
                del self.list_items[i]
