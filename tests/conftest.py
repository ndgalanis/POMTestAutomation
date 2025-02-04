import pytest
from utils.singleton_driver import SingletonDriver

@pytest.fixture(scope="function", autouse=True)
def cleanup_after_test():
    SingletonDriver.quit_driver()
