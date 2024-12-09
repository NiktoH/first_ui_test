import allure

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.login = (By.ID, 'user-name')           #Локатор по ID для элемента строки ввода login
        self.password = (By.ID, 'password')         #Локатор по ID для элемента строки ввода password
        self.login_btn = (By.NAME, 'login-button')  #Локатор по Name для элемента кнопка Login

    @allure.step(r"Ввести логин и пароль")
    def auth(self, login: str, password: str) -> None:
        self.find_element(*self.login).send_keys(login)
        self.find_element(*self.password).send_keys(password)
        self.find_element(*self.login_btn).click()
