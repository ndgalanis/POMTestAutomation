from models.model_actions.user_actions import UserActions

class UserData:

    def __init__(self, first_name=None, last_name=None, email=None, password=None):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._birthdate = None
        self._actions = UserActions(self)

    def actions(self):
        return self._actions

    def get_first_name(self): return self._first_name
    def get_last_name(self): return self._last_name
    def get_full_name(self): return f'{self._first_name} {self._last_name}'
    def get_email(self): return self._email
    def get_password(self): return self._password
    def get_birthdate(self): return self._birthdate # Avoid returning plain passwords in real apps!

    def set_first_name(self, first_name): self._first_name = first_name
    def set_last_name(self, last_name): self._last_name = last_name
    def set_email(self, email): self._email = email
    def set_password(self, password): self._password = password
    def set_birthdate(self, birthdate): self._birthdate = birthdate
