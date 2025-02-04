from pages.base_page import BasePage

class AddUser(BasePage):
    """
    AddUser page object representing the user registration page.
    Inherits from BasePage and provides methods to interact with the user registration form.
    """

    def __init__(self):
        """
        Initializes the AddUser page with a predefined URL and title.
        """
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/addUser'
        self.title = 'Add User'

    def get_page_title(self):
        """
        Returns the XPath expression for verifying the page title.

        :return: XPath string for the page title.
        """
        return f'//title[contains(text(), "{self.title}")]'

    @staticmethod
    def get_path_submit_button():
        """
        Returns the XPath for the submit button.

        :return: XPath string for the submit button.
        """
        return '//button[@id="submit"]'

    @staticmethod
    def get_path_first_name_field():
        """
        Returns the XPath for the first name input field.

        :return: XPath string for the first name field.
        """
        return '//Input[@id="firstName"]'

    @staticmethod
    def get_path_last_name_field():
        """
        Returns the XPath for the last name input field.

        :return: XPath string for the last name field.
        """
        return '//Input[@id="lastName"]'

    @staticmethod
    def get_path_email_field():
        """
        Returns the XPath for the email input field.

        :return: XPath string for the email field.
        """
        return '//Input[@id="email"]'

    @staticmethod
    def get_path_password_field():
        """
        Returns the XPath for the password input field.

        :return: XPath string for the password field.
        """
        return '//Input[@id="password"]'

    def click_submit_button(self):
        """
        Clicks the submit button to submit the form.
        """
        self.click_element(self.get_path_submit_button())

    def enter_first_name(self, first_name):
        """
        Enters text into the first name input field.

        :param first_name: The first name to enter.
        """
        self.enter_text(self.get_path_first_name_field(), first_name)

    def enter_last_name(self, last_name):
        """
        Enters text into the last name input field.

        :param last_name: The last name to enter.
        """
        self.enter_text(self.get_path_last_name_field(), last_name)

    def enter_email(self, email):
        """
        Enters text into the email input field.

        :param email: The email address to enter.
        """
        self.enter_text(self.get_path_email_field(), email)

    def enter_password(self, password):
        """
        Enters text into the password input field.

        :param password: The password to enter.
        """
        self.enter_text(self.get_path_password_field(), password)

    def check_title(self):
        """
        Verifies that the Add User page title is displayed.

        :return: True if the title is found, otherwise raises an exception.
        """
        self.element_exists(self.get_page_title())
