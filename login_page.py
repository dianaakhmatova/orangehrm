from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.CSS_SELECTOR, ".orangehrm-login-button")

    def login(self, user, passwd):
        self.fill(self.username, user)
        self.fill(self.password, passwd)
        self.click(self.login_btn)
