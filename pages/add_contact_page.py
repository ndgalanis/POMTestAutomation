from pages.base_page import BasePage

class AddContact(BasePage):

    def __init__(self):
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/addContact'
        self.title = 'Add Contact'

    def get_page_title(self):
        return f'//title[contains(text(), "{self.title}")]'

    @staticmethod
    def get_path_first_name_field():
        return '//Input[@id="firstName"]'

    @staticmethod
    def get_path_last_name_field():
        return '//Input[@id="lastName"]'

    @staticmethod
    def get_path_birthdate_field():
        return '//input[@id="birthdate"]'

    @staticmethod
    def get_path_birthdate_error():
        return "//span[@id='error' and contains(text(), 'Birthdate is invalid')]"

    @staticmethod
    def get_path_submit_button():
        return '//button[@id="submit"]'

    def enter_birthdate(self, birthdate):
        self.enter_text(self.get_path_birthdate_field(), birthdate)

    def enter_first_name(self, first_name):
        self.enter_text(self.get_path_first_name_field(), first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.get_path_last_name_field(), last_name)

    def check_birthdate_error_exists(self):
        self.element_exists(self.get_path_birthdate_error())

    def click_submit_button(self):
        self.click_element(self.get_path_submit_button())
        from pages.contact_list_page import ContactList
        landing_page = ContactList()
        return landing_page

    def check_title(self):
        self.element_exists(self.get_page_title())
