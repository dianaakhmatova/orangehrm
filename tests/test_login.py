import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.title("Успешный вход в систему")
@allure.description("Проверка, что пользователь с правильными данными входит в систему.")
def test_successful_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_dashboard_displayed()

@allure.title("Неуспешный вход в систему")
@allure.description("Проверка, что пользователь с неправильными данными не входит.")
def test_invalid_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(driver)
    login_page.login("Admin", "wrongpass")
    error = driver.find_element("css selector", ".oxd-alert-content-text")
    assert "Invalid" in error.text