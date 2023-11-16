import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def write(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def check_elements_exists(self, locator):
        assert self.find_element(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela!"

    def get_text_element(self, locator):
        self.waiting_element_appear(locator)
        return self.find_element(locator).text


    def waiting_element_appear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    def check_element_exist(self, locator):
        assert self.find_element(locator), f"Elemento '{locator}' não existe, mas é esperado que ele exista."

    def check_element_not_exist(self, locator):
        assert len(self.find_element(locator)) == 0, f"Elemento '{locator}' existe, mas o espero não é que ele exista"

    def double_click_method(self, locator):
        element = self.waiting_element_appear(locator)
        ActionChains(self.driver).double_click(element).perform()

    def click_right_btn(self, locator):
        element = self.waiting_element_appear(locator)
        ActionChains(self.driver).context_click(element).perform()
    def press_keyboard_key(self, locator, key):
        elem = self.find_element(locator)
        if key == 'ENTER':
            elem.send_keys(Keys.ENTER)
        elif key == 'SPACE':
            elem.send_keys(Keys.SPACE)
        elif key == 'F1':
            elem.send_keys(Keys.F1)
        elif key == 'F5':
            elem.send_keys(Keys.F5)
        elif key == 'ARROW_LEFT':
            elem.send_keys(Keys.ARROW_LEFT)
        elif key == 'ARROW_RIGHT':
            elem.send_keys(Keys.ARROW_RIGHT)
        elif key == 'ESC':
            elem.send_keys(Keys.ESCAPE)
        elif key == 'HOME':
            elem.send_keys(Keys.HOME)







