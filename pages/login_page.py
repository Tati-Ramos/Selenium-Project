import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.usarname_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        # self.driver.find_element(*self.usarname_field).send_keys(usuario)
        # self.driver.find_element(*self.password_field).send_keys(senha)
        # self.driver.find_element(*self.login_button).click()
        self.write(self.usarname_field, usuario)
        self.write(self.password_field, senha)
        self.click(self.login_button)
