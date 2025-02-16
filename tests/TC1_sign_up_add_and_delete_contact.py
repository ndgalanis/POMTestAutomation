from test_data.users import generate_random_user

class TestSignUpAddAndDeleteContact:

    USER_1 = generate_random_user()
    USER_2 = generate_random_user()

    def test_sign_up(self):
        """
        Test case for signing up a new user.

        This test uses USER_1's data to perform the sign-up process by filling out the registration form
        and submitting it. It verifies that the sign-up process is completed successfully.
        """
        self.USER_1.actions().sign_up()

    def test_add_contact(self):
        """
        Test case for adding a contact to USER_1's contact list.

        This test logs in as USER_1 and adds USER_2 to their contact list. It verifies that the contact
        is successfully added by checking if the contact's full name appears in the list.
        """
        self.USER_1.actions().add_contact(self.USER_2)

    def test_delete_contact(self):
        """
        Test case for deleting a contact from USER_1's contact list.

        This test logs in as USER_1, selects USER_2 from their contact list, and deletes the contact.
        It verifies that the contact is successfully removed by checking that the contact's name no longer
        appears in the list.
        """
        self.USER_1.actions().delete_contact(self.USER_2)
