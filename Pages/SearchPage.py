from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class SearchPage(BasePage):
    search_field = (By.ID, "APjFqb")
    search_button = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/div/span/svg")


