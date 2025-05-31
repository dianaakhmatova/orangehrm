import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

@allure.title("Успешный вход в систему")
def test_successful_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_displayed()
    assert "dashboard" in driver.current_url.lower()

@allure.title("Неверный пароль")
def test_login_wrong_password(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(driver)
    login_page.login("Admin", "wrongpass")
    error = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text")
    assert "Invalid" in error.text
    assert error.is_displayed()