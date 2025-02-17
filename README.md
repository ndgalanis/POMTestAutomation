# About the Project
POMTestAutomation contains automated tests for the Thinking Tester Contact List web application, utilizing 
**Python**, **Selenium**, and **pytest**. The tests are written to run with Google Chrome but can be adapted to other 
browsers as needed.

The **Page Object Model** (POM) is a pattern that separates the test logic from page-specific elements, 
making the tests more maintainable. Each page of the application (e.g., sign up, contact list) is 
represented by a separate class, which encapsulates the interactions with that page.

# Key Features
- **Singleton Design Pattern**: Uses the Singleton pattern to manage WebDriver instances, 
                                ensuring only one instance is created throughout each test execution.
                                This is optimized for parallel test runs.
- **Dynamic Navigator**: Implements dynamic navigation logic to handle seamless transitions between pages.
- **Pytest Parallel Execution**: `pytest` is configured in `pytest.ini` to run a maximum of 5 test files<> 
                                  simultaneously, starting with files that begin with "TC".

# Installation
1. Clone the repository: 
    ```bash
    git clone https://github.com/your-username/POMTestAutomation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd POMTestAutomation
    ```
3. Create a virtual environment:
    - On Windows: 
      ```bash
      python -m venv venv
      ```
    - On macOS: 
      ```bash
      python3 -m venv venv
      ```
4. Activate the virtual environment:
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS:
      ```bash
      source venv/bin/activate
      ```
5. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

# How to Run Tests
- Open the terminal in your IDE and run:
  ```bash
  pytest
