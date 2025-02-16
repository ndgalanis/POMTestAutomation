from pages.page_utils.page_navigator import PageNavigator

class UserActions:
    """
    A class that performs various user actions such as signing up, logging in,
    adding and deleting contacts.
    """

    def __init__(self, user_data):
        """
        Initializes the UserActions class with user data.

        :param user_data: The user data object containing user information (e.g., first name, email).
        """
        self.user_data = user_data
        self.navigator = PageNavigator()

    def sign_up(self):
        """
        Performs the sign-up process for a new user by entering user data and submitting the form.
        Navigates through the starting page to the sign-up form by clicking the SignUp button,
        enters the details, and submits.

        :return: None
        """
        page1 = self.navigator.navigate_to("starting_page")
        page2 = page1.click_sign_up_button()
        page2.check_title()
        page2.enter_first_name(self.user_data.get_first_name())
        page2.enter_last_name(self.user_data.get_last_name())
        page2.enter_email(self.user_data.get_email())
        page2.enter_password(self.user_data.get_password())
        page2.click_submit_button()

    def add_contact(self, new_contact):
        """
        Adds a new contact for the logged-in user.

        This method logs in first, then navigates to the 'Add Contact' page, enters the contact's details,
        and submits the form. Afterward, it checks if the contact was successfully added in the Contact List Page.

        :param new_contact: The user object containing contact details (e.g., first name, last name).
        :return: None
        """
        page1 = self.log_in()
        page2 = page1.click_add_contact_button()
        page2.check_title()
        page2.enter_first_name(new_contact.get_first_name())
        page2.enter_last_name(new_contact.get_last_name())
        page3 = page2.click_submit_button()
        page3.check_title()
        page3.check_name_exists(new_contact.get_full_name())

    def log_in(self):
        """
        Logs in the user by navigating through the starting page, entering the credentials,
        and submitting the login form.

        :return: The page object after the user has logged in.
        """
        page1 = self.navigator.navigate_to("starting_page")
        page1.check_title()
        page1.enter_email(self.user_data.get_email())
        page1.enter_password(self.user_data.get_password())
        page2 = page1.click_submit_button()
        page2.check_title()
        return page2

    def delete_contact(self, contact_to_delete):
        """
        Deletes an existing contact for the logged-in user.

        This method logs in first, then navigates to the contact's details page, clicks the delete button,
        and confirms the deleted user is no longer visible  in the Contact List Page.

        :param contact_to_delete: The user object containing contact information (e.g., full name).
        :return: None
        """
        page1 = self.log_in()
        page2 = page1.click_contact_name(contact_to_delete.get_full_name())
        page2.check_title()
        page2.click_delete_contact_button()
        page3 = page2.click_ok_in_delete_alert()
        page3.check_title()
        page3.check_name_not_exists(contact_to_delete.get_last_name())

    def check_invalid_birthdate_error_for_new_contact(self, user_with_invalid_birthdate):
        """
        Checks for an invalid birthdate error while adding a new contact.

        This method logs in first, navigates to the 'Add Contact' page, enters a valid first name, a valid last name,
        an invalid birthdate, and submits the form. Then, it verifies that the error message appears.

        :param user_with_invalid_birthdate: The user object containing contact details (including birthdate).
        :return: None
        """
        page1 = self.log_in()
        page2 = page1.click_add_contact_button()
        page2.check_title()
        page2.enter_first_name(user_with_invalid_birthdate.get_first_name())
        page2.enter_last_name(user_with_invalid_birthdate.get_last_name())
        page2.enter_birthdate(user_with_invalid_birthdate.get_birthdate())
        page2.click_submit_button()
        page2.check_birthdate_error_exists()
