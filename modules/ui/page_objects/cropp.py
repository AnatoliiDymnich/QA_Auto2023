from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class Cropp_shop(BasePage):
    def __init__(self, item_name):
        super().__init__()
        self.item_name = item_name

    def go_to(self):
        self.driver.get(f'https://www.cropp.com/ua/uk/{self.item_name}')

    def add_to_cart(self):
        cookie_button = self.driver.find_element(By.ID, 'cookiebotDialogOkButton')
        cookie_button.click()

        add_to_cart = self.driver.find_element(By.CLASS_NAME, 'add-to-cart-text')
        add_to_cart.click()
        self.driver.implicitly_wait(1)

        go_to_cart = self.driver.find_element(By.XPATH, "//a[@data-selen='cart-confirmation-go-to-checkout']")
        go_to_cart.click()
        self.driver.implicitly_wait(1)

    def check_cart(self):
        return self.item_name in self.driver.page_source

