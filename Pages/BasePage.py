from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).click()

    def send_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return element.text

    def is_enable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is(title))
        return self.driver.title



