"""
User class
"""

import re


class UserOps(object):
    """
    Code to handle registration and log in of users
    """

    def __init__(self):
        # list to contain users
        self.user_list = []

    def register(self, username, password, cpassword):
        """
        Registers users
        Arguments:
            username: string
            password: string
        Returns:
            Status message
        """
        # empty dict to hold each user
        user_dict = {}
        # check for existing user
        for user in self.user_list:
            if username == user['username']:
                return "The user already exists."
        else:
            # check for password length and mismatch
            if len(password) < 6:
                return "The password should be at least 6 characters long"
            elif password != cpassword:
                return "The passwords do not match"
            elif not re.match("^[a-zA-Z0-9_]*$", username):
                return "The username cannot contain special characters. Only underscores"
            else:
                user_dict['username'] = username
                user_dict['password'] = password
                self.user_list.append(user_dict)
                return "Registered successfully"

    def login(self, username, password):
        """
        Args
            email(string):user email
            userpassword(string):password
        Return
            error msg or success msg
        Purpose
            Login users
        """
        for user in self.user_list:
            if username == user['username']:
                if password == user['password']:
                    return "Login successful"
                else:
                    return "The passwords do not match"
        return "The user does not exist"
