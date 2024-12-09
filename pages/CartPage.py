import allure

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.check_contains_product = (By.XPATH, '//div[@class="cart_item"]//div[@class="inventory_item_name"]')
        self.item_list = (By.XPATH, '//div[@class="cart_item"]')
        self.check_price_product = (By.XPATH, '//div[@class="cart_item"]//div[@class="inventory_item_price"]')
        self.checkout_btn = (By.XPATH, '//*[@id= "checkout"]')

    @allure.step(r"Найти количество товаров")
    def number_of_products(self):
        return len(self.find_elements(*self.item_list))

    @allure.step(r"Проверить, что товар содержит своё название")
    def find_contains_product(self):
        return self.find_element(*self.check_contains_product).text

    @allure.step(r"Кликнуть по кнопке checkout")
    def checkout_btn_click(self):
        self.find_element(*self.checkout_btn).click()

    @allure.step(r"")
    def find_price_product(self):
        return float(self.find_element(*self.check_price_product).text[1:])