import allure

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.contains_product = (By.XPATH, '//div[@class="cart_item"]//div[@class="inventory_item_name"]')
        self.item_list = (By.XPATH, '//div[@class="cart_item"]')
        self.price_product = (By.XPATH, '//div[@class="cart_item"]//div[@class="inventory_item_price"]')
        self.checkout_btn = (By.XPATH, '//*[@id= "checkout"]')

    @allure.step(r"Найти количество товаров")
    def number_of_products(self) -> int:
        return len(self.find_elements(*self.item_list))

    @allure.step(r"Получить значение названия товара")
    def get_title_product(self) -> str:
        return self.find_element(*self.contains_product).text

    @allure.step(r"Кликнуть по кнопке checkout")
    def checkout_btn_click(self) -> None:
        self.find_element(*self.checkout_btn).click()

    @allure.step(r"Получить цену товара")
    def find_price_product(self) -> float:
        return float(self.find_element(*self.price_product).text[1:])