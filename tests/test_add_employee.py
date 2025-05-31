import pytest
import allure
from selenium.webdriver.common.by import By
import time

@allure.title("Добавление нового сотрудника")
def test_add_employee(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()
    driver.find_element(By.LINK_TEXT, "PIM").click()
    driver.find_element(By.LINK_TEXT, "Add Employee").click()
    driver.find_element(By.NAME, "firstName").send_keys("Test")
    driver.find_element(By.NAME, "lastName").send_keys("User")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    success = driver.find_element(By.TAG_NAME, "h6").text
    assert "Personal Details" in success
    assert driver.current_url.endswith("viewPersonalDetails/empNumber")