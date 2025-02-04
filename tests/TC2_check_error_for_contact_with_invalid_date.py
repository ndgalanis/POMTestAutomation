from test_data.users import user_3, user_4

class TestSignUpAndAddUser:

    USER_1 = user_3()
    USER_2 = user_4()
    BIRTHDATE = "abc"

    def test_set_up(self):
        self.USER_1.actions().sign_up()

    def test_sign_up(self):
        self.USER_1.actions().check_invalid_birthdate_error_for_new_contact(self.USER_2)
