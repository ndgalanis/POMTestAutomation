from pages.base_page import BasePage

class AddUser(BasePage):

    def __init__(self):
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/addUser'

    @staticmethod
    def get_path_submit_button():
        return '//button[@id="submit"]'

    @staticmethod
    def get_path_first_name_field():
        return '//Input[@id="firstName"]'

    @staticmethod
    def get_path_last_name_field():
        return '//Input[@id="lastName"]'

    @staticmethod
    def get_path_email_field():
        return '//Input[@id="email"]'

    @staticmethod
    def get_path_password_field():
        return '//Input[@id="password"]'

    def click_submit_button(self):
        self.click_element(self.get_path_submit_button())

    def enter_first_name(self, first_name):
        self.enter_text(self.get_path_first_name_field(), first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.get_path_last_name_field(), last_name)

    def enter_email(self, email):
        self.enter_text(self.get_path_email_field(), email)

    def enter_password(self, password):
        self.enter_text(self.get_path_password_field(), password)
