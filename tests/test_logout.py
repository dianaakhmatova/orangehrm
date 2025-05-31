import pytest
import allure
from selenium.webdriver.common.by import By
import time

@allure.title("Выход из системы")
def test_logout(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()
    driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(1)
    assert "login" in driver.current_url.lower()
    assert driver.find_element(By.NAME, "username").is_displayed()