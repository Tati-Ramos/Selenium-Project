import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
time.sleep(2)

password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)

login_btn = driver.find_element(By.ID, "login-button").click()
time.sleep(2)

assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
time.sleep(1)

driver.quit()