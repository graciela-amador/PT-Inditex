from selenium.webdriver.common.by import By
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains


def test_search_automation_in_google():
    """
    Test that performs a google search with the word "Automation", checks the year of the first automated process
    and takes a screenshot of the result.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.es/')
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div').click()
    driver.find_element(By.ID, 'APjFqb').send_keys('automatización')
    driver.find_element(By.XPATH, "//html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]").click()
    driver.find_element(By.XPATH, '//div/div/a/h3[text()="Automatización - Wikipedia, la enciclopedia libre"]').click()
    first_automated_process = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[text()[contains(., "1785")]]')
    assert first_automated_process.is_displayed()
    actions = ActionChains(driver)
    actions.move_to_element(first_automated_process).perform()
    driver.save_screenshot('screen_test.png')
    screenshot = Image.open('screen_test.png')
    screenshot.show()
