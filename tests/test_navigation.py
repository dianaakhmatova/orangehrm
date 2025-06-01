import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage

@allure.title("Переход в раздел Admin")
@allure.description("Тест проверки перехода в модуль Admin и отображения списка пользователей.")
def test_navigate_to_admin(driver):
    with allure.step("Авторизация в системе"):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        LoginPage(driver).login("Admin", "admin123")
    with allure.step("Переход в раздел Admin"):
        DashboardPage(driver).go_to_admin()
    admin_page = AdminPage(driver)
    with allure.step("Проверяем, что отобразился раздел System Users"):
        assert admin_page.is_system_users_displayed(), "Раздел 'System Users' не отображается!"
