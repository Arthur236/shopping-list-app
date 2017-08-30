"""
User class
"""
class User(object):
    """
    Code for user registration and sign in
    """

    def __init__(self):
        """
        Initialize variables
        """
        self.user_list = []

    def create_user(self, username, password, cpassword): 
        """
        Registers new users    
        Arguments:
            username: string -- user name
            password: string -- password
            cpassword: string -- password
        Returns:
            Status message
        """
        user_dict = {}
        #check if user is already registered
        for user in self.user_list:
            if username == user['username']:
                return "The user already exists."
            else:
                #check if password is long enough
                if len(password) < 6:
                    return "The password should be at least 6 characters long"
                elif password == cpassword:
                    user_dict['username'] = username
                    user_dict['password'] = password
                    self.user_list.append(user_dict)
                else:
                    return "The passwords do not match"
            return "Successfully registered."

        def sign_in(self, username, password):
            """
            Sign in registered users
            Arguments:
                username: string -- user name
                password: string -- password
            Returns:
            Status message
            """
            for user in self.user_list:
                if username == user['username']:
                    if password == user['password']:
                        return "Sign in successful"
                    else:
                        return "Passwords do not match"
            return "User does not exist"
