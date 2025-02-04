from selenium import webdriver

class SingletonDriver:
    _driver = None

    @staticmethod
    def get_driver():
        """Get the single WebDriver instance."""
        if SingletonDriver._driver is None:
            SingletonDriver._driver = webdriver.Chrome()
        return SingletonDriver._driver

    @staticmethod
    def quit_driver():
        """Quit the WebDriver if it's initialized."""
        if SingletonDriver._driver:
            SingletonDriver._driver.quit()
            SingletonDriver._driver = None
