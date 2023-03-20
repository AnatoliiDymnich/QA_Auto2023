import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(
        service=Service(r'C:\Users\toli\QA_Auto2023' + 'chromedriver.exe')
        )

    driver.get('https://github.com/login')

    login_elem = driver.find_element(By.ID, 'login_field')
    pass_elem = driver.find_element(By.ID, 'password')
    enter_elem = driver.find_element(By.NAME, 'commit')

    login_elem.send_keys("wrongemail@gemeil.com")
    pass_elem.send_keys("wrongpassword")
    enter_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()
