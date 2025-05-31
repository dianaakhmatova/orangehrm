import pytest
import allure
from selenium.webdriver.common.by import By

@allure.title("Навигация по сайдбару")
@allure.description("Проверка доступности разделов сайта через сайдбар.")
def test_sidebar_navigation(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button.orangehrm-login-button").click()
    sidebar = driver.find_elements(By.CLASS_NAME, "oxd-main-menu-item")
    assert len(sidebar) > 5