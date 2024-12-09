import allure

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.item_list = (By.XPATH, '//*[@class= "cart_item"]')
        self.check_contains_product = (By.XPATH, '//div[@class="cart_item"]//div[@class="inventory_item_name"]')
        self.check_payment_information = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "Payment Information")]')
        self.check_payment_value = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "SauceCard #31337")]')
        self.check_shipping_information = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "Shipping Information")]')
        self.check_shipping_value = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "Free Pony Express Delivery!")]')
        self.check_price_total_information = (By.XPATH, '//*[@class="summary_info"]/*[contains(text(), "Price Total")]')
        self.check_price_subtotal_information = (By.CSS_SELECTOR, '[data-test="subtotal-label"]')
        self.check_tax_label = (By.CSS_SELECTOR, '[data-test="tax-label"]')
        self.check_total_label = (By.CSS_SELECTOR, '[data-test="total-label"]')
        self.finish_btn = (By.ID, 'finish')


    @allure.step(r"Найти заголовок Payment Information")
    def find_payment_information(self):
        return self.find_element(*self.check_payment_information).text

    @allure.step(r"Найти значение SauceCard")
    def find_payment_value(self):
        return self.find_element(*self.check_payment_value).text

    @allure.step(r"Найти заголовок Shipping information")
    def find_shipping_information(self):
        return self.find_element(*self.check_shipping_information).text

    @allure.step(r"Найти значение Free Pony Express Delivery")
    def find_shipping_value(self):
        return self.find_element(*self.check_shipping_value).text

    @allure.step(r"Найти итоговую цену")
    def find_price_total_information(self):
        return self.find_element(*self.check_price_total_information).text

    @allure.step(r"Найти цену предмета")
    def find_price_subtotal_information(self):
        return self.find_element(*self.check_price_subtotal_information).text[:11]

    @allure.step(r"Найти цену")
    def find_price_subtotal_value(self):
        return float(self.find_element(*self.check_price_subtotal_information).text[13:])

    @allure.step(r"Найти налог")
    def find_tax_label(self):
        return self.find_element(*self.check_tax_label).text[:4]

    @allure.step(r"Найти цену налога")
    def find_price_tax_value(self):
        return float(self.find_element(*self.check_tax_label).text[6:])

    @allure.step(r"Найти итог")
    def find_total_label(self):
        return self.find_element(*self.check_total_label).text[:6]

    @allure.step(r"Найти цену итога")
    def find_price_total_value(self):
        return float(self.find_element(*self.check_total_label).text[8:])

    @allure.step(r"Кликнуть по кнопке finish")
    def finish_btn_click(self):
        self.find_element(*self.finish_btn).click()

    @allure.step(r"Найти количество товаров")
    def number_of_products(self):
        return len(self.find_elements(*self.item_list))

    @allure.step(r"Проверить, что товар содержит своё название")
    def find_contains_products(self):
        return self.find_element(*self.check_contains_product).text