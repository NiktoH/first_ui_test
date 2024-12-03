from pages import BasePage, LoginPage, InventoryPage, ItemPage, CartPage
import allure


@allure.title(r"Проверка добавления товаров в корзину")
def test_est_1_login(driver):
    auth_page = LoginPage(driver)
    auth_page.auth('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)
    inventory_page.choose_item()

    item_page = ItemPage(driver)
    item_page.add_to_cart_btn_click()
    item_page.back_to_products()

    inventory_page.add_jacket_to_cart_btn_click()
    inventory_page.cart_btn_click()

    cart_page = CartPage(driver)
    with allure.step(r"Проверка количества товаров"):
        assert cart_page.number_of_products() == 2, "Неверное количество элементов в корзине"


@allure.title(r"Проверка авторизации с правильными данными")
def test_auth(driver):
    auth_page = LoginPage(driver)
    auth_page.input_login('standard_user')
    auth_page.input_password('secret_sauce')
    auth_page.login_button_click()

    InventoryPage(driver).check_inventory_page_open()


@allure.title(r"Проверка авторизации с неправильными данными")
def test_fail_auth(driver):
    auth_page = LoginPage(driver)
    auth_page.input_login('standard_user')
    auth_page.input_password('BestPassword123')
    auth_page.login_button_click()

    InventoryPage(driver).check_inventory_page_close()