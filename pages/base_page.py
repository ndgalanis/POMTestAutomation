from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.singleton_driver import SingletonDriver

class BasePage:

    def __init__(self):
        self.driver = SingletonDriver.get_driver()

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, xpath):
        try:
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except (NoSuchElementException, TimeoutException):
            raise NoSuchElementException

    def enter_text(self, xpath, text):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.clear()
            element.send_keys(text)
        except NoSuchElementException:
            raise NoSuchElementException

    def get_text(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            raise NoSuchElementException

    def element_exists(self, xpath):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            raise TimeoutException(f"Element with xpath '{xpath}' not found within 3 seconds.")
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with xpath '{xpath}' does not exist.")

    def element_not_exists(self, xpath, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            raise Exception(f"Element with xpath '{xpath}' should not exist but was found.")
        except TimeoutException:
            return True
        except NoSuchElementException:
            return True

    def alert_accept(self):
        try:
            Alert(self.driver).accept()
            return True
        except NoAlertPresentException:
            raise NoAlertPresentException

    def close_browser(self):
        if self.driver:
            self.driver.quit()
