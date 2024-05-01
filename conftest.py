import pytest
from selenium import webdriver
from locators import Url

@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(chrome_options)
    chrome_driver.get(Url.main)
    yield chrome_driver
    chrome_driver.quit()
