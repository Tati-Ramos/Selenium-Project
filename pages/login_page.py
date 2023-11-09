import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.usarname_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//div[@class='error-message-container error']//h3[@data-test='error']")

    def fazer_login(self, usuario, senha):
        # self.driver.find_element(*self.usarname_field).send_keys(usuario)
        # self.driver.find_element(*self.password_field).send_keys(senha)
        # self.driver.find_element(*self.login_button).click()
        self.write(self.usarname_field, usuario)
        self.write(self.password_field, senha)
        self.click(self.login_button)

    def check_message_error_login_exist(self):
        self.check_elements_exists(self.error_message_login)

    def check_message_text_login(self, expected_text):
        text_found = self.get_text_element(self.error_message_login)
        assert text_found == expected_text, f"O texto encontrado foi '{text_found}', mas era esperado o texto '{expected_text}'."


