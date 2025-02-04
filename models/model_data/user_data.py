from models.model_actions.user_actions import UserActions

class UserData:
    """
    A class that holds user data such as first name, last name, email, password, and birthdate.
    Provides methods for getting and setting user information and also interacting with user actions.
    """

    def __init__(self, first_name=None, last_name=None, email=None, password=None):
        """
        Initializes the UserData class with optional user details.

        :param first_name: The user's first name.
        :param last_name: The user's last name.
        :param email: The user's email address.
        :param password: The user's password.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._birthdate = None
        self._actions = UserActions(self)

    def actions(self):
        """
        Returns the UserActions instance associated with this user.

        :return: The UserActions object that handles user-specific actions.
        """
        return self._actions

    def get_first_name(self):
        """
        Returns the user's first name.

        :return: The first name of the user.
        """
        return self._first_name

    def get_last_name(self):
        """
        Returns the user's last name.

        :return: The last name of the user.
        """
        return self._last_name

    def get_full_name(self):
        """
        Returns the user's full name by concatenating first and last names.

        :return: The full name of the user (first name + last name).
        """
        return f'{self._first_name} {self._last_name}'

    def get_email(self):
        """
        Returns the user's email.

        :return: The email address of the user.
        """
        return self._email

    def get_password(self):
        """
        Returns the user's password. Avoid returning plain passwords in real applications.

        :return: The password of the user.
        """
        return self._password

    def get_birthdate(self):
        """
        Returns the user's birthdate.

        :return: The birthdate of the user (can be None if not set).
        """
        return self._birthdate

    def set_first_name(self, first_name):
        """
        Sets the user's first name.

        :param first_name: The new first name to set.
        """
        self._first_name = first_name

    def set_last_name(self, last_name):
        """
        Sets the user's last name.

        :param last_name: The new last name to set.
        """
        self._last_name = last_name

    def set_email(self, email):
        """
        Sets the user's email address.

        :param email: The new email to set.
        """
        self._email = email

    def set_password(self, password):
        """
        Sets the user's password.

        :param password: The new password to set.
        """
        self._password = password

    def set_birthdate(self, birthdate):
        """
        Sets the user's birthdate.

        :param birthdate: The new birthdate to set.
        """
        self._birthdate = birthdate
