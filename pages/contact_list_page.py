from pages.base_page import BasePage

class ContactList(BasePage):

    def __init__(self):
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/contactList'
        self.title = 'My Contacts'

    def get_page_title(self):
        return f'//title[contains(text(), "{self.title}")]'

    @staticmethod
    def get_path_add_contact_button():
        return '//button[@id="add-contact"]'

    @staticmethod
    def get_path_contact_name(name):
        return f'//td[contains(text(), "{name}")]'

    def click_add_contact_button(self):
        self.click_element(self.get_path_add_contact_button())
        from pages.add_contact_page import AddContact
        landing_page = AddContact()
        return landing_page
    
    def click_contact_name(self, name):
        self.click_element(self.get_path_contact_name(name))
        from pages.contact_details_page import ContactDetails
        landing_page = ContactDetails()
        return landing_page

    def check_name_exists(self, name):
        self.element_exists(self.get_path_contact_name(name))

    def check_name_not_exists(self, name):
        self.element_not_exists(self.get_path_contact_name(name))

    def check_title(self):
        self.element_exists(self.get_page_title())
