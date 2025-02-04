from pages.base_page import BasePage

class StartingPage(BasePage):

    def __init__(self):
        super().__init__()
        self.url = 'https://thinking-tester-contact-list.herokuapp.com/'
        self.title = 'Contact List App'

    def get_page_title(self):
        return f'//title[contains(text(), "{self.title}")]'

    def get_page_url(self):
        return self.url

    @staticmethod
    def get_path_sign_up_button():
        return '//button[@id="signup"]'

    @staticmethod
    def get_path_email_field():
        return '//Input[@id="email"]'

    @staticmethod
    def get_path_password_field():
        return '//Input[@id="password"]'

    @staticmethod
    def get_path_submit_button():
        return '//button[@id="submit"]'

    def click_sign_up_button(self):
        path = self.get_path_sign_up_button()
        self.click_element(path)
        from pages.add_user_page import AddUser
        landing_page = AddUser()
        landing_page.check_title()
        return landing_page

    def enter_email(self, email):
        self.enter_text(self.get_path_email_field(), email)

    def enter_password(self, password):
        self.enter_text(self.get_path_password_field(), password)

    def click_submit_button(self):
        self.click_element(self.get_path_submit_button())
        from pages.contact_list_page import ContactList
        landing_page = ContactList()
        return landing_page

    def check_title(self):
        self.element_exists(self.get_page_title())