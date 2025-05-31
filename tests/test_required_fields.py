import pytest
import allure
from selenium.webdriver.common.by import By

@allure.title("Проверка обязательных полей")
def test_required_fields(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()
    driver.find_element(By.LINK_TEXT, "PIM").click()
    driver.find_element(By.LINK_TEXT, "Add Employee").click()
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_messages = driver.find_elements(By.CLASS_NAME, "oxd-input-field-error-message")
    assert len(error_messages) >= 2
    for msg in error_messages:
        assert "Required" in msg.text