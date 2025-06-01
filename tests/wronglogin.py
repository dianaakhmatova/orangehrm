import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Негативный тест: неверный логин в OrangeHRM")
@allure.description("Проверка ошибки при вводе неверных учетных данных")
def test_wrong_login():
    driver = webdriver.Chrome()

    with allure.step("Открытие страницы OrangeHRM"):
        driver.get("https://opensource-demo.orangehrmlive.com/")

    with allure.step("Ввод некорректного логина и пароля"):
        driver.find_element(By.NAME, "username").send_keys("wrong")
        driver.find_element(By.NAME, "password").send_keys("wrongpass")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

    with allure.step("Проверка отсутствия перехода в систему"):
        assert "dashboard" not in driver.current_url

    driver.quit()
