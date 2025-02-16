from test_data.users import generate_random_user, user_with_wrong_birthdate_format

class TestErrorMessageForNewContactWithInvalidBirthdate:

    USER_1 = generate_random_user()
    USER_2 = user_with_wrong_birthdate_format()

    def test_set_up(self):
        """
        Test case for setting up a new user.

        This test case performs the sign-up process for USER_1, which includes entering the necessary
        details (name, email, password) to complete the registration.
        """
        self.USER_1.actions().sign_up()

    def test_sign_up(self):
        """
        Test case for checking invalid birthdate error during new contact addition.

        This test case attempts to add a new contact (USER_2) with an invalid birthdate ("abc") and
        verifies that an error message related to the invalid birthdate is displayed.
        """
        self.USER_1.actions().check_invalid_birthdate_error_for_new_contact(self.USER_2)
