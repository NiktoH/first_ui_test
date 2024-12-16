import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.BasePage import BasePage


class FinishPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.title_field = (By.XPATH, '//*[@class="title"]')
        self.complete_header = (By.XPATH, '//h2[@class="complete-header"]')
        self.complete_text = (By.XPATH, '//*[@class="complete-text"]')
        self.back_home_btn = (By.ID, 'back-to-products')

    @allure.step(r"Проверить наличие поля Checkout: Complete!")
    def check_title(self) -> str:
        return self.get_text(self.title_field)

    @allure.step(r"Получить заголовок Thank you for your order!")
    def get_complete_header(self) -> str:
        return self.get_text(self.complete_header)

    @allure.step(r"Проверить наличие заголовка Your order has been dispatched, and will arrive just as fast as the pony can get there!")
    def get_complete_text(self) -> str:
        return self.get_text(self.complete_text)

    @allure.step(r"Проверить наличие кнопки Back Home")
    def find_back_home_btn(self) -> WebElement:
        return self.get_element(self.back_home_btn)
