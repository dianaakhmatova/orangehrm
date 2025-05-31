import pytest
import allure
from selenium.webdriver.common.by import By

@allure.title("Поиск сотрудника")
@allure.description("Проверка поиска сотрудника по имени.")
def test_search_employee(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()
    driver.find_element(By.LINK_TEXT, "PIM").click()
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']").send_keys("Paul")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    result = driver.find_element(By.XPATH, "//div[@role='table']//div[contains(text(),'Paul')]")
    assert "Paul" in result.text