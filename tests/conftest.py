import pytest as pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def username_password():
    user_name = "Frith"
    password = "22222"

    return [user_name, password]


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()
