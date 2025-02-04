from pages.base_page import BasePage


class ContactList(BasePage):
    """
    ContactList page object representing the contact list page in the application.
    Inherits from BasePage and provides methods to interact with the contact list page.
    """

    def __init__(self):
        """
        Initializes the ContactList page with a predefined URL and title.
        """
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/contactList'
        self.title = 'My Contacts'

    def get_page_title(self):
        """
        Returns the XPath expression for verifying the page title.

        :return: XPath string for the page title.
        """
        return f'//title[contains(text(), "{self.title}")]'

    @staticmethod
    def get_path_add_contact_button():
        """
        Returns the XPath for the "Add Contact" button.

        :return: XPath string for the add contact button.
        """
        return '//button[@id="add-contact"]'

    @staticmethod
    def get_path_contact_name(name):
        """
        Generates the XPath for locating a contact by name.

        :param name: The name of the contact.
        :return: XPath string for locating the contact.
        """
        return f'//td[contains(text(), "{name}")]'

    def click_add_contact_button(self):
        """
        Clicks the "Add Contact" button and navigates to the Add Contact page.

        :return: An instance of the AddContact page object.
        """
        self.click_element(self.get_path_add_contact_button())
        from pages.add_contact_page import AddContact
        return AddContact()

    def click_contact_name(self, name):
        """
        Clicks on a contact name and navigates to the Contact Details page.

        :param name: The name of the contact to click.
        :return: An instance of the ContactDetails page object.
        """
        self.click_element(self.get_path_contact_name(name))
        from pages.contact_details_page import ContactDetails
        return ContactDetails()

    def check_name_exists(self, name):
        """
        Checks if a contact name exists in the contact list.

        :param name: The name of the contact to check.
        :return: True if the contact exists, otherwise raises an exception.
        """
        self.element_exists(self.get_path_contact_name(name))

    def check_name_not_exists(self, name):
        """
        Checks that a contact name does not exist in the contact list.

        :param name: The name of the contact to check.
        :return: True if the contact does not exist, otherwise raises an exception.
        """
        self.element_not_exists(self.get_path_contact_name(name))

    def check_title(self):
        """
        Verifies that the contact list page title is displayed.

        :return: True if the title is found, otherwise raises an exception.
        """
        self.element_exists(self.get_page_title())
