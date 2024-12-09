import allure

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_btn = (By.ID, 'continue')


    @allure.step(r"Ввести Имя, Фамилию, Код")
    def checkout_auth(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.find_element(*self.first_name).send_keys(first_name)
        self.find_element(*self.last_name).send_keys(last_name)
        self.find_element(*self.postal_code).send_keys(postal_code)


    @allure.step(r"Кликнуть по кнопке continue")
    def continue_btn_click(self):
        self.find_element(*self.continue_btn).click()
