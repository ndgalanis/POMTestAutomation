from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.singleton_driver import SingletonDriver


class BasePage:
    """
    BasePage is a parent class that provides common Selenium WebDriver methods
    for interacting with web elements in a test automation framework.
    """

    def __init__(self):
        """Initializes the BasePage and retrieves the WebDriver instance."""
        self.driver = SingletonDriver.get_driver()

    def open_page(self, url: str):
        """
        Opens a webpage using the given URL.

        :param url: The URL of the webpage to open.
        """
        self.driver.get(url)

    def click_element(self, xpath: str):
        """
        Clicks an element found by the provided XPath.

        :param xpath: The XPath of the element to click.
        :raises NoSuchElementException: If the element is not found within the timeout.
        """
        try:
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except (NoSuchElementException, TimeoutException):
            raise NoSuchElementException(f"Element with xpath '{xpath}' not found or not clickable.")

    def enter_text(self, xpath: str, text: str):
        """
        Enters text into an input field found by XPath.

        :param xpath: The XPath of the input field.
        :param text: The text to enter.
        :raises NoSuchElementException: If the element is not found.
        """
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.clear()
            element.send_keys(text)
        except NoSuchElementException:
            raise NoSuchElementException(f"Input field with xpath '{xpath}' not found.")

    def get_text(self, xpath: str):
        """
        Retrieves the text content of an element found by XPath.

        :param xpath: The XPath of the element.
        :return: The text content of the element.
        :raises NoSuchElementException: If the element is not found.
        """
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with xpath '{xpath}' not found.")

    def element_exists(self, xpath: str):
        """
        Checks if an element exists within a given timeout.

        :param xpath: The XPath of the element.
        :return: True if the element is found, otherwise raises an exception.
        :raises TimeoutException: If the element is not found within the timeout.
        :raises NoSuchElementException: If the element does not exist.
        """
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            raise TimeoutException(f"Element with xpath '{xpath}' not found within 3 seconds.")

    def element_not_exists(self, xpath: str, timeout=5):
        """
        Checks if an element does not exist within a given timeout.

        :param xpath: The XPath of the element.
        :param timeout: The time in seconds to wait before confirming absence.
        :return: True if the element does not exist, False if it appears.
        :raises Exception: If the element is unexpectedly found.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            raise Exception(f"Element with xpath '{xpath}' should not exist but was found.")
        except TimeoutException:
            return True

    def alert_accept(self):
        """
        Accepts an alert if present.

        :return: True if the alert is successfully accepted.
        :raises NoAlertPresentException: If no alert is present.
        """
        try:
            Alert(self.driver).accept()
            return True
        except NoAlertPresentException:
            raise NoAlertPresentException("No alert found to accept.")

    def close_browser(self):
        """
        Closes the browser and quits the WebDriver session.
        """
        if self.driver:
            self.driver.quit()

    def refresh_browser(self):
        """
        Refreshes the browser.
        """
        if self.driver:
            self.driver.refresh()