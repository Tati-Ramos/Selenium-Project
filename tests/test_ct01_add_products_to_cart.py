import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import conftest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("https://www.saucedemo.com/")

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.cart
class TestCT01:
    def test_ct01_add_products_to_cart(self):
        #driver = conftest.driver
        #Login
        # username = driver.find_element(By.ID, "user-name")
        # username.send_keys("standard_user")
        # time.sleep(2)
        # password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # time.sleep(2)
        # login_btn = driver.find_element(By.ID, "login-button").click()
        # time.sleep(2)

        # instância os objetos a serem usados no teste
        login_page = LoginPage()
        # faz o login
        login_page.fazer_login("standard_user", "secret_sauce")

        home_page = HomePage()
        cart_page = CartPage()

        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Bike Light"

        #Add Product to cart: backpack1
        # click_on_the_product1 = driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
        # time.sleep(2)
        # add_to_cart1 = driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        # time.sleep(2)
        home_page.add_to_cart(product_1)


        #shopping_cart_link = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()


        #checking that the backpack has been added to the cart
        #assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        home_page.access_cart()
        cart_page.check_products_cart_exist(product_1)
        time.sleep(2)


        # #Continue shopping and returning to the products page
        # continue_shopping = driver.find_element(By.ID, "continue-shopping").click()
        cart_page.click_keep_buying()
        time.sleep(1)



        # #Adding the second product to the cart
        # click_on_the_product2 = driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
        # time.sleep(2)
        # add_to_cart2= driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        home_page.add_to_cart(product_2)
        time.sleep(2)


        # shopping_cart_link = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()


        # #checking that the two backpacks have been added to the cart
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        # time.sleep(1)
        # assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
        home_page.access_cart()
        cart_page.check_products_cart_exist(product_1)
        cart_page.check_products_cart_exist(product_2)
        time.sleep(2)

        # #checkout
        # driver.find_element(By.ID, "checkout").click()
        # assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Checkout: Your Information']")
        # time.sleep(1)
        # first_name = driver.find_element(By.ID,"first-name").send_keys("Teste")
        # time.sleep(1)
        # last_name = driver.find_element(By.ID, "last-name").send_keys("Funcional")
        # time.sleep(1)
        # postal_code = driver.find_element(By.ID, "postal-code").send_keys("24472290")
        #
        # continue_btn = driver.find_element(By.ID, "continue").click()
        # assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Checkout: Overview']")
        # time.sleep(2)
        #
        # finish_btn = driver.find_element(By.ID, "finish").click()
        # assert driver.find_element(By.XPATH, "//span[@class='title' and text()='Checkout: Complete!']")
        # assert driver.find_element(By.XPATH, "//h2[@class='complete-header' and text()='Thank you for your order!']")
        # time.sleep(2)
        #
        #







#driver.quit()