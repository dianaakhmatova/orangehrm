import allure
from pages.login_page import LoginPage
from pages.leave_page import LeavePage

def test_apply_leave(driver):
    login = LoginPage(driver)
    driver.get("https://opensource-demo.orangehrmlive.com")
    login.login("Admin", "admin123")
    leave = LeavePage(driver)
    leave.apply_leave("2025-06-01", "2025-06-05", "Vacation")
    assert "Leave" in driver.page_source
