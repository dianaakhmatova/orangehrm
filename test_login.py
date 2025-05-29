import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(driver):
    login = LoginPage(driver)
    driver.get("https://opensource-demo.orangehrmlive.com")
    login.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    assert "Dashboard" in dashboard.get_header()

def test_invalid_login(driver):
    login = LoginPage(driver)
    driver.get("https://opensource-demo.orangehrmlive.com")
    login.login("invalid", "wrongpass")
    assert "Invalid credentials" in driver.page_source
