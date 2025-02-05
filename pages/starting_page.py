from pages.base_page import BasePage

class StartingPage(BasePage):
    """
    StartingPage page object representing the application's starting page (login/signup).
    Inherits from BasePage and provides methods to interact with the login and sign-up options.
    """

    def __init__(self):
        """
        Initializes the StartingPage with a predefined URL and title.
        """
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/'
        self.title = 'Contact List App'

    def get_page_title(self):
        """
        Returns the XPath expression for verifying the page title.

        :return: XPath string for the page title.
        """
        return f'//title[contains(text(), "{self.title}")]'

    def get_page_url(self):
        """
        Returns the page URL.

        :return: URL string of the page.
        """
        return self.url

    @staticmethod
    def get_path_sign_up_button():
        """
        Returns the XPath for the sign-up button.

        :return: XPath string for the sign-up button.
        """
        return '//button[@id="signup"]'

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

    @staticmethod
    def get_path_submit_button():
        """
        Returns the XPath for the submit button.

        :return: XPath string for the submit button.
        """
        return '//button[@id="submit"]'

    def click_sign_up_button(self):
        """
        Clicks the sign-up button to navigate to the Add User page.

        :return: An instance of the AddUser page object.
        """
        path = self.get_path_sign_up_button()
        self.click_element(path)
        from pages.add_user_page import AddUserPage
        landing_page = AddUserPage()
        landing_page.check_title()
        return landing_page

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

    def click_submit_button(self):
        """
        Clicks the submit button to log in and navigates to the ContactList page.

        :return: An instance of the ContactList page object.
        """
        self.click_element(self.get_path_submit_button())
        from pages.contact_list_page import ContactListPage
        return ContactListPage()

    def check_title(self):
        """
        Verifies that the page title is displayed.

        :return: True if the title is found, otherwise raises an exception.
        """
        self.element_exists(self.get_page_title())
