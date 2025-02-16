from selenium import webdriver

class SingletonDriver:
    """
    A singleton class for managing the Selenium WebDriver instance.
    Ensures that only one instance of WebDriver is created and reused throughout the test execution.
    """

    _driver = None

    @staticmethod
    def get_driver():
        """
        Retrieves the single WebDriver instance. If the driver is not initialized, it creates a new one.

        :return: The WebDriver instance.
        """
        if SingletonDriver._driver is None:
            SingletonDriver._driver = webdriver.Chrome()
        return SingletonDriver._driver

    @staticmethod
    def quit_driver():
        """
        Quits the WebDriver if it is initialized and resets the instance to None.

        This ensures proper cleanup of resources and prevents memory leaks.
        """
        if SingletonDriver._driver:
            SingletonDriver._driver.quit()
            SingletonDriver._driver = None
