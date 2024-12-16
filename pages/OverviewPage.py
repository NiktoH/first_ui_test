import allure
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.item_list = (By.XPATH, '//*[@class= "cart_item"]')
        self.contains_product = (By.XPATH, '//div[@class="cart_item"]//div[@class="inventory_item_name"]')
        self.payment_information = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "Payment Information")]')
        self.payment_value = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "SauceCard #31337")]')
        self.shipping_information = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "Shipping Information")]')
        self.shipping_value = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "Free Pony Express Delivery!")]')
        self.price_total_information = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "Price Total")]')
        self.price_subtotal_information = (By.CSS_SELECTOR, '[data-test="subtotal-label"]')
        self.tax_label = (By.CSS_SELECTOR, '[data-test="tax-label"]')
        self.total_label = (By.CSS_SELECTOR, '[data-test="total-label"]')
        self.finish_btn = (By.ID, 'finish')


    @allure.step(r"Найти заголовок Payment Information")
    def find_payment_information(self) -> str:
        return self.get_text(self.payment_information)

    @allure.step(r"Найти значение SauceCard")
    def find_payment_value(self) -> str:
        return self.get_text(self.payment_value)

    @allure.step(r"Найти заголовок Shipping information")
    def find_shipping_information(self) -> str:
        return self.get_text(self.shipping_information)

    @allure.step(r"Найти значение Free Pony Express Delivery")
    def find_shipping_value(self) -> str:
        return self.get_text(self.shipping_value)

    @allure.step(r"Найти итоговую цену")
    def find_price_total_information(self) -> str:
        return self.get_text(self.price_total_information)

    @allure.step(r"Найти цену предмета")
    def find_price_subtotal_information(self) -> str:
        return self.get_text(self.price_subtotal_information)[:11]

    @allure.step(r"Найти цену")
    def find_price_subtotal_value(self) -> float:
            return float(self.get_text(self.price_subtotal_information)[13:])

    @allure.step(r"Найти налог")
    def find_tax_label(self) -> str:
           return self.get_text(self.tax_label)[:4]

    @allure.step(r"Найти цену налога")
    def find_price_tax_value(self) -> float:
        return float(self.get_text(self.tax_label)[6:])

    @allure.step(r"Найти итог")
    def find_total_label(self) -> str:
        return self.get_text(self.total_label)[:6]

    @allure.step(r"Найти цену итога")
    def find_price_total_value(self) -> float:
        return float(self.get_text(self.total_label)[8:])

    @allure.step(r"Кликнуть по кнопке finish")
    def finish_btn_click(self):
        self.click_element(self.finish_btn)

    @allure.step(r"Найти количество товаров")
    def number_of_products(self) -> int:
        return len(self.find_elements(*self.item_list))

    @allure.step(r"Проверить, что товар содержит своё название")
    def find_contains_products(self) -> str:
        return self.get_text(self.contains_product)