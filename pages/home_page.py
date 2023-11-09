from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.inventory_item= (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")
        self.add_to_cart_btn = (By.XPATH, "//*[text()='Add to cart']")
        self.cart_icon = (By.XPATH, "//*[@class='shopping_cart_link']")

    def check_login_successfully(self):
        self.check_elements_exists(self.page_title)

    def add_to_cart(self, item_name):
        item = (self.inventory_item[0], self.inventory_item[1].format(item_name))
        self.click(item)
        self.click(self.add_to_cart_btn)

    def access_cart(self):
        self.click(self.cart_icon)