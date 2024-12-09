import allure

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.add_tshirt_to_cart_btn = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        self.check_cart_number = (By.XPATH, '//*[@class="shopping_cart_link"]/span[contains(text(), "1")]')
        self.cart_btn = (By.XPATH, '//*[@class="shopping_cart_link"]')

    @allure.step(r"Добавить футболку в корзину")
    def add_tshirt_to_cart_btn_click(self):
        self.find_element(*self.add_tshirt_to_cart_btn).click()

    @allure.step(r"Найти цифру рядом с корзиной")
    def find_cart_number(self):
        return len(self.find_elements(*self.check_cart_number))

    @allure.step(r"Кликнуть по корзине")
    def cart_btn_click(self):
        self.find_element(*self.cart_btn).click()
