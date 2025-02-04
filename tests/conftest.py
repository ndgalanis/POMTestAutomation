import pytest
from utils.singleton_driver import SingletonDriver

@pytest.fixture(scope="function", autouse=True)
def cleanup_after_test():
    """
    A pytest fixture that ensures the WebDriver is quit after each test function is executed.

    This fixture is automatically applied before and after each test function,
    ensuring that the WebDriver is properly cleaned up and no resources are leaked.
    """
    SingletonDriver.quit_driver()
