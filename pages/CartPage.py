import allure
from selenium.common import NoSuchElementException

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
    def number_of_products(self):
        return len(self.find_elements(*self.item_list))

    @allure.step(r"Получить значение названия товара")
    def get_title_product(self) -> str:
        return self.get_text(self.contains_product)

    @allure.step(r"Кликнуть по кнопке checkout")
    def checkout_btn_click(self) -> None:
        self.click_element(self.checkout_btn)

    @allure.step(r"Получить цену товара")
    def find_price_product(self) -> float:
        try:
            return float(self.find_element(*self.price_product).text[1:])
        except NoSuchElementException:
            print("Элемент 'цена' не найден")

