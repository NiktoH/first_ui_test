import allure
from pages.FinishPage import FinishPage
from pages.CheckoutPage import CheckoutPage
from pages.CartPage import CartPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from pages.BasePage import BasePage
from pages.OverviewPage import OverviewPage


def test_est_1_login(driver):
    auth_page = LoginPage(driver)
    auth_page.auth('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)
    inventory_page.add_tshirt_to_cart_btn_click()
    with allure.step(r"Проверка наличия цифры рядом с корзиной"):
        assert inventory_page.find_cart_number(), "Цифры рядом с корзиной не найдена"
    inventory_page.cart_btn_click()

    cart_page = CartPage(driver)
    with allure.step(r"Проверка количества товаров"):
        assert cart_page.number_of_products() == 1

    with allure.step(r"Проверка названия содержимого "):
        assert cart_page.find_contains_product()

    with allure.step(r"Проверка цены"):
        assert cart_page.find_price_product()

    cart_page.checkout_btn_click()

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout_auth('Masha', 'Smirnova', '432001')
    checkout_page.continue_btn_click()

    overview_page = OverviewPage(driver)
    with allure.step(r"Проверка количества товаров"):
        assert overview_page.number_of_products() == 1

    with allure.step(r"Проверка названия содержимого"):
        assert overview_page.find_contains_products()

    with allure.step(r"Поиск заголовка Payment Information"):
        assert overview_page.find_payment_information()

    with allure.step(r"Поиск значения SauceCard"):
        assert overview_page.find_payment_value()

    with allure.step(r"Поиск заголовка Shipping information"):
        assert overview_page.find_shipping_information()

    with allure.step(r"Поиск значения Free Pony Express Delivery"):
        assert overview_page.find_shipping_value()

    with allure.step(r"Поиск итоговой цены(текста Итоговая цена)"):
        assert overview_page.find_price_total_information()

    with allure.step(r"Поиск итоговой цены(текста)"):
        assert overview_page.find_price_subtotal_information()

    with allure.step(r"Поиск итоговой цены"):
        assert overview_page.find_price_subtotal_value()

    with allure.step(r"Поиск налога(текста)"):
        assert overview_page.find_tax_label()

    with allure.step(r"Поиск налога"):
        assert overview_page.find_price_tax_value()

    with allure.step(r"Поиск итога"):
        assert overview_page.find_total_label()

    with allure.step(r"Поиск цены итога"):
        assert overview_page.find_price_total_value()

    overview_page.finish_btn_click()

    finish_page = FinishPage(driver)
    with allure.step(r"Проверка наличия поля Checkout: Complete!"):
        assert finish_page.check_title()

    with allure.step(r"Проверка наличия заголовка Thank you for your order!"):
        assert finish_page.find_complete_header()

    with allure.step(r"Проверка наличия заголовка Your order has been dispatched, and will arrive just as fast as the pony can get there!"):
        assert finish_page.find_complete_text()

    with allure.step(r"Проверка наличия кнопки Back Home"):
        assert finish_page.find_back_home_btn()