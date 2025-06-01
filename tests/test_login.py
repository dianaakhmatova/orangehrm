import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.title("Успешный вход в систему")
@allure.description("Тест проверяет, что пользователь с корректными учетными данными может войти в систему.")
def test_successful_login(driver):
    with allure.step("Открываем страницу авторизации OrangeHRM"):
        driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(driver)
    with allure.step("Вводим правильный логин и пароль"):
        login_page.login("Admin", "admin123")
    dashboard_page = DashboardPage(driver)
    with allure.step("Проверяем, что отобразился дашборд"):
        assert dashboard_page.is_dashboard_displayed(), "Dashboard не отображается, вход не выполнен!"

@allure.title("Вход с неверными учетными данными")
@allure.description("Тест проверяет, что при вводе некорректных учетных данных отображается сообщение об ошибке.")
def test_invalid_login(driver):
    with allure.step("Открываем страницу авторизации OrangeHRM"):
        driver.get("https://opensource-demo.orangehrmlive.com/")
    login_page = LoginPage(driver)
    with allure.step("Вводим неверный логин и пароль"):
        login_page.login("wrong_user", "wrong_pass")
    with allure.step("Проверяем, что появилось сообщение об ошибке"):
        # Ожидаем текст "Invalid credentials" на странице
        error_message = driver.find_element_by_xpath("//p[contains(@class,'oxd-alert-content-text')]").text
        assert "Invalid credentials" in error_message, "Отсутствует сообщение об ошибке при неверном входе"
pytest --alluredir=allure-results

