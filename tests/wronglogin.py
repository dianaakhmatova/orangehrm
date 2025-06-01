from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Запуск браузера
service = Service("/opt/homebrew/bin/chromedriver")
browser = webdriver.Chrome(service=service)

# Переход на страницу входа
browser.get("https://opensource-demo.orangehrmlive.com/")

# Ждём поля
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username")))

# Ввод неверных данных
browser.find_element(By.NAME, "username").send_keys("WrongUser")
browser.find_element(By.NAME, "password").send_keys("wrongpass")
browser.find_element(By.XPATH, "//button[@type='submit']").click()

# Ждём сообщение об ошибке
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Invalid')]"))
)

# Скриншот ошибки
browser.save_screenshot("5_invalid_login.png")
browser.quit()
pytest --alluredir=allure-results
allure serve allure-results

