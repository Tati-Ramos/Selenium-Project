import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

#Login
username = driver.find_element(By.ID, "user-name")
username.send_keys("teste")
time.sleep(2)
password = driver.find_element(By.ID, "password").send_keys("1234")
time.sleep(2)
login_btn = driver.find_element(By.ID, "login-button").click()
assert driver.find_element(By.XPATH, "//div[@class='error-message-container error']//h3[@data-test='error']")
time.sleep(2)
