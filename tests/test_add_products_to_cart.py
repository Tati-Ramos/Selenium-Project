import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

#Login
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
time.sleep(2)
password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
login_btn = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

#Add Product to cart: backpack1
click_on_the_product1 = driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()
time.sleep(2)
add_to_cart1 = driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
time.sleep(2)

shopping_cart_link = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

#checking that the backpack has been added to the cart
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
time.sleep(2)

#Continue shopping and returning to the products page
continue_shopping = driver.find_element(By.ID, "continue-shopping").click()

#Adding the second product to the cart
click_on_the_product2 = driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()
time.sleep(2)
add_to_cart2= driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
time.sleep(2)

shopping_cart_link = driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

#checking that the two backpacks have been added to the cart
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
time.sleep(1)
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
time.sleep(1)


driver.quit()