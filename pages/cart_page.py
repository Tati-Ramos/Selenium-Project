from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.inventory_item = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.keep_buying_btn = (By.ID, "continue-shopping")

    def check_products_cart_exist(self, item_name):
        item = (self.inventory_item[0], self.inventory_item[1].format(item_name))
        self.check_elements_exists(item)

    def click_keep_buying(self):
        self.click(self.keep_buying_btn)
