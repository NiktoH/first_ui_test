import allure

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
        return self.find_element(*self.payment_information).text

    @allure.step(r"Найти значение SauceCard")
    def find_payment_value(self) -> str:
        return self.find_element(*self.payment_value).text

    @allure.step(r"Найти заголовок Shipping information")
    def find_shipping_information(self) -> str:
        return self.find_element(*self.shipping_information).text

    @allure.step(r"Найти значение Free Pony Express Delivery")
    def find_shipping_value(self) -> str:
        return self.find_element(*self.shipping_value).text

    @allure.step(r"Найти итоговую цену")
    def find_price_total_information(self) -> str:
        return self.find_element(*self.price_total_information).text

    @allure.step(r"Найти цену предмета")
    def find_price_subtotal_information(self) -> str:
        return self.find_element(*self.price_subtotal_information).text[:11]

    @allure.step(r"Найти цену")
    def find_price_subtotal_value(self) -> float:
        return float(self.find_element(*self.price_subtotal_information).text[13:])

    @allure.step(r"Найти налог")
    def find_tax_label(self) -> str:
        return self.find_element(*self.tax_label).text[:4]

    @allure.step(r"Найти цену налога")
    def find_price_tax_value(self) -> float:
        return float(self.find_element(*self.tax_label).text[6:])

    @allure.step(r"Найти итог")
    def find_total_label(self) -> str:
        return self.find_element(*self.total_label).text[:6]

    @allure.step(r"Найти цену итога")
    def find_price_total_value(self) -> float:
        return float(self.find_element(*self.total_label).text[8:])

    @allure.step(r"Кликнуть по кнопке finish")
    def finish_btn_click(self):
        self.find_element(*self.finish_btn).click()

    @allure.step(r"Найти количество товаров")
    def number_of_products(self) -> int:
        return len(self.find_elements(*self.item_list))

    @allure.step(r"Проверить, что товар содержит своё название")
    def find_contains_products(self) -> str:
        return self.find_element(*self.contains_product).text