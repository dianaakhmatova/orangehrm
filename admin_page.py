from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminPage(BasePage):
    admin_tab = (By.LINK_TEXT, "Admin")
    add_button = (By.XPATH, "//button[text()=' Add ']")
    username_input = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
    save_button = (By.XPATH, "//button[@type='submit']")

    def open_admin_tab(self):
        self.click(self.admin_tab)

    def add_user(self, username):
        self.click(self.add_button)
        self.fill(self.username_input, username)
        self.click(self.save_button)
