import allure

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class FinishPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.check_title_field = (By.XPATH, '//*[@class="title"]')
        self.check_complete_header = (By.XPATH, '//h2[@class="complete-header"]')
        self.check_complete_text = (By.XPATH, '//*[@class="complete-text"]')
        self.check_back_home_btn = (By.ID, 'back-to-products')

    @allure.step(r"Проверить наличие поля Checkout: Complete!")
    def check_title(self):
        return self.find_element(*self.check_title_field).text

    @allure.step(r"Проверить наличие заголовка Thank you for your order!")
    def find_complete_header(self):
        return self.find_element(*self.check_complete_header).text

    @allure.step(r"Проверить наличие заголовка Your order has been dispatched, and will arrive just as fast as the pony can get there!")
    def find_complete_text(self):
        return self.find_element(*self.check_complete_text).text

    @allure.step(r"Проверить наличие кнопки Back Home")
    def find_back_home_btn(self):
        return self.find_element(*self.check_back_home_btn)
