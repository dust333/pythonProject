import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Edge(executable_path='./msedgedriver.exe')
    yield driver
    driver.quit()
