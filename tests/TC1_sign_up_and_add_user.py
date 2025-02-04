from test_data.users import user_1, user_2

class TestSignUpAndAddUser:

    USER_1 = user_1()
    USER_2 = user_2()

    def test_sign_up(self):
        self.USER_1.actions().sign_up()

    def test_add_contact(self):
        self.USER_1.actions().add_contact(self.USER_2)

    def test_delete_contact(self):
        self.USER_1.actions().delete_contact(self.USER_2)
