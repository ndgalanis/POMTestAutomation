from models.model_data.user_data import UserData
from random import randint

"""
This file contains functions that generate test user data for automated tests.

Each function creates an instance of the UserData class.
"""

def generate_random_user():
    user = UserData()
    user.set_first_name(f'Random First Name {randint(1, 100)}')
    user.set_last_name(f'Random Lest Name{randint(1, 100)}')
    user.set_email(f'random_email_{randint(1, 100)}@rndmemail123.com')
    user.set_password('test123')
    return user

def user_with_wrong_birthdate_format():
    user = generate_random_user()
    user.set_birthdate('12345')
    return user
