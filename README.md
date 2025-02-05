This repository contains automated tests for Thinking Tester Contact List using Python, pytest, and Selenium.
Runs with Google Chrome.

Test Cases:

--------------------------------------------------

TC1:

Step 1:
- Sign up with a new user

Step 2:
- Log in with the new user
- Add a new contact
- Validate the contact has been added

Step 3:
- Log in with the new user
- Delete the new contact
- Validate the contact has been deleted

--------------------------------------------------

TC2:

Step 1:
- Sign up with a new user

Step 2:
- Log in with the new user
- Navigate to the add contact page
- Enter a valid first name
- Enter a valid last name
- Enter invalid birthdate
- Click Submit
- Validate birthdate error message

--------------------------------------------------
