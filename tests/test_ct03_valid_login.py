import time

import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage


# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("https://www.saucedemo.com/")
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_valid_login(self):
       #driver = conftest.driver

        #instância os objetos a serem usados no teste
        login_page = LoginPage()
        #faz o login
        login_page.fazer_login("standard_user", "secret_sauce")

       # instância os objetos a serem usados no teste
        home_page = HomePage()
        #verifica se o login foi realizado com sucesso
        home_page.check_login_successfully()

        # username = driver.find_element(By.ID, "user-name")
        # username.send_keys("standard_user")
        # time.sleep(2)
        #
        # password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # time.sleep(2)
        #
        # login_btn = driver.find_element(By.ID, "login-button").click()
        # time.sleep(2)

        #assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
        time.sleep(1)
