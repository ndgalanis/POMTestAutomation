from pages.base_page import BasePage

class ContactDetails(BasePage):
    """
    ContactDetails page object representing the contact details page in the application.
    Inherits from BasePage and provides methods to interact with the contact details page.
    """

    def __init__(self):
        """
        Initializes the ContactDetails page with a predefined URL.
        """
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/contactDetails'
        self.title = ''

    def get_page_title(self):
        """
        Returns the XPath expression for verifying the page title.

        :return: XPath string for the page title.
        """
        return f'//title[contains(text(), "{self.title}")]'

    @staticmethod
    def get_path_delete_contact_button():
        """
        Returns the XPath for the delete contact button.

        :return: XPath string for the delete button.
        """
        return '//button[@id="delete"]'

    def click_delete_contact_button(self):
        """
        Clicks the delete contact button.
        """
        self.click_element(self.get_path_delete_contact_button())

    def click_ok_in_alert(self):
        """
        Clicks OK in the alert dialog that appears after deleting a contact.
        Redirects back to the ContactList page.

        :return: An instance of the ContactList page object.
        """
        self.alert_accept()
        from pages.contact_list_page import ContactList
        return ContactList()

    def check_title(self):
        """
        Verifies that the contact details page title is displayed.

        :return: True if the title is found, otherwise raises an exception.
        """
        self.element_exists(self.get_page_title())
