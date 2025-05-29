import allure
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_user(driver):
    login = LoginPage(driver)
    driver.get("https://opensource-demo.orangehrmlive.com")
    login.login("Admin", "admin123")
    admin = AdminPage(driver)
    admin.open_admin_tab()
    admin.add_user("testuser123")
    assert "testuser123" in driver.page_source
