import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r'C:\Users\toli\QA_Auto2023' + 'chromedriver.exe')
        )

    # відкриваємо сторінку
    driver.get('https://github.com/login')

    # знаходимо потрібне поле
    login_elem = driver.find_element(By.ID, 'login_field')
    pass_elem = driver.find_element(By.ID, 'password')
    enter_elem = driver.find_element(By.NAME, 'commit')

    # ввести дані
    login_elem.send_keys("wrongemail@gemeil.com")
    pass_elem.send_keys("wrongpassword")
    enter_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"

    # закрити браузер

