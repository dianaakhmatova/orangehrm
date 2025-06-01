from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("/opt/homebrew/bin/chromedriver")
browser = webdriver.Chrome(service=service)

browser.get("https://opensource-demo.orangehrmlive.com/")
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username")))

# Логин
browser.find_element(By.NAME, "username").send_keys("Admin")
browser.find_element(By.NAME, "password").send_keys("admin123")
browser.find_element(By.XPATH, "//button[@type='submit']").click()

# Переход в PIM
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']")))
browser.find_element(By.XPATH, "//span[text()='PIM']").click()

# Кликаем Add Employee
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Add Employee']")))
browser.find_element(By.XPATH, "//a[text()='Add Employee']").click()

# Заполняем форму
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "firstName")))
browser.find_element(By.NAME, "firstName").send_keys("Diana")
browser.find_element(By.NAME, "lastName").send_keys("Testova")

# Сохраняем
browser.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)
browser.save_screenshot("6_add_employee.png")
browser.quit()
