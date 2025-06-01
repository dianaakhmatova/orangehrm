# Поиск сотрудника “Paul” в PIM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("/opt/homebrew/bin/chromedriver")
browser = webdriver.Chrome(service=service)
browser.get("https://opensource-demo.orangehrmlive.com/")
browser.maximize_window()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username")))
browser.find_element(By.NAME, "username").send_keys("Admin")
browser.find_element(By.NAME, "password").send_keys("admin123")
browser.find_element(By.XPATH, "//button[@type='submit']").click()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='PIM']")))
browser.find_element(By.XPATH, "//span[text()='PIM']").click()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
browser.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Paul")
browser.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(2)
browser.save_screenshot("3_search_result.png")
importlib(dsg)
