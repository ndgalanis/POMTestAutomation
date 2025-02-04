from pages.navigator import Navigator
from time import sleep
class UserActions:

    def __init__(self, user_data):
        self.user_data = user_data
        self.navigate_to = Navigator()

    def sign_up(self):
        page1 = self.navigate_to.starting_page()
        page2 = page1.click_sign_up_button()
        page2.check_title()
        page2.enter_first_name(self.user_data.get_first_name())
        page2.enter_last_name(self.user_data.get_last_name())
        page2.enter_email(self.user_data.get_email())
        page2.enter_password(self.user_data.get_password())
        page2.click_submit_button()

    def add_contact(self, user):
        page1 = self.log_in()
        page2 = page1.click_add_contact_button()
        page2.check_title()
        page2.enter_first_name(user.get_first_name())
        page2.enter_last_name(user.get_last_name())
        page3 = page2.click_submit_button()
        page3.check_title()
        page3.check_name_exists(user.get_full_name())

    def log_in(self):
        page1 = self.navigate_to.starting_page()
        page1.check_title()
        page1.enter_email(self.user_data.get_email())
        page1.enter_password(self.user_data.get_password())
        page2 = page1.click_submit_button()
        page2.check_title()
        return page2

    def delete_contact(self, user):
        page1 = self.log_in()
        page2 = page1.click_contact_name(user.get_full_name())
        page2.check_title()
        page2.click_delete_contact_button()
        page3 = page2.click_ok_in_alert()
        page3.check_title()
        page3.check_name_not_exists(user.get_last_name())

    def check_invalid_birthdate_error_for_new_contact(self, user):
        page1 = self.log_in()
        page2 = page1.click_add_contact_button()
        page2.check_title()
        page2.enter_birthdate(user.get_birthdate())
        page2.click_submit_button()
        page2.check_birthdate_error_exists()
