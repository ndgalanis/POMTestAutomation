import pytest
from utils.singleton_driver import SingletonDriver

@pytest.fixture(scope="function", autouse=True)
def cleanup_after_test():
    """Fixture that will clean up WebDriver after each test function."""
    yield  # Test function execution happens here
    SingletonDriver.quit_driver()  # Cleanup (quit WebDriver) after each test
