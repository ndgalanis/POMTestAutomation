from models.model_data.user_data import UserData
from random import randint

"""
This file contains functions that generate test user data for automated tests.

Each function creates an instance of the UserData class.
"""

def user_1():
    user = UserData()
    user.set_first_name(f'Robert_{randint(1, 100)}')
    user.set_last_name(f'Smith_{randint(1, 100)}')
    user.set_email(f'test{randint(1, 100)}@vimac123.com')
    user.set_password('test123')
    return user

def user_2():
    user = UserData()
    user.set_first_name(f'Mike_{randint(1, 100)}')
    user.set_last_name(f'Shinoda_{randint(1, 100)}')
    user.set_email(f'test_{randint(1, 100)}@vimac123.com')
    user.set_password('test123')
    return user

def user_3():
    user = UserData()
    user.set_first_name(f'Bruce_{randint(1, 100)}')
    user.set_last_name(f'Wayne_{randint(1, 100)}')
    user.set_email(f'test_{randint(1, 100)}@vimac123.com')
    user.set_password('test123')
    return user

def user_4():
    user = UserData()
    user.set_first_name(f'Darth_{randint(1, 100)}')
    user.set_last_name(f'Vader_{randint(1, 100)}')
    user.set_email(f'test_{randint(1, 100)}@vimac123.com')
    user.set_password('test123')
    user.set_birthdate('12345')
    return user
