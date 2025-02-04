from pages.base_page import BasePage

class ContactDetails(BasePage):

    def __init__(self):
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/contactDetails'
        self.title = ''

    def get_page_title(self):
        return f'//title[contains(text(), "{self.title}")]'

    @staticmethod
    def get_path_delete_contact_button():
        return '//button[@id="delete"]'

    def click_delete_contact_button(self):
        self.click_element(self.get_path_delete_contact_button())

    def click_ok_in_alert(self):
        self.alert_accept()
        from pages.contact_list_page import ContactList
        landing_page = ContactList()
        return landing_page

    def check_title(self):
        self.element_exists(self.get_page_title())