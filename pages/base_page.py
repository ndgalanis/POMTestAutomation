from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.singleton_driver import SingletonDriver

class BasePage:

    def __init__(self):
        """Ensure driver is available in the BasePage and child classes."""
        #self.driver = globals.SELENIUM_DRIVER
        self.driver = SingletonDriver.get_driver()

    def open_page(self, url):
        """Open a webpage."""
        self.driver.get(url)

    def click_element(self, xpath):
        """Click an element using XPath. Only accessible within subclasses."""
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element(By.XPATH, xpath).click()
        except NoSuchElementException:
            raise NoSuchElementException

    def enter_text(self, xpath, text):
        """Enter text into an input field. Only accessible within subclasses."""
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.clear()
            element.send_keys(text)
        except NoSuchElementException:
            raise NoSuchElementException

    def get_text(self, xpath):
        """Retrieve text from an element. Only accessible within subclasses."""
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            return None  # Return None if element is not found

    def element_exists(self, xpath):
        """Check if an element exists on the page. Only accessible within subclasses."""
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            raise NoSuchElementException

    def element_not_exists(self, xpath, timeout=5):
        """Check if an element does NOT exist within the given timeout."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return False  # Element still exists
        except TimeoutException:
            return True

    def alert_accept(self):
        """Accept a browser alert if present. Only accessible within subclasses."""
        try:
            Alert(self.driver).accept()
            return True
        except NoAlertPresentException:
            return False

    def close_browser(self):
        """Close the browser."""
        if self.driver:
            self.driver.quit()
