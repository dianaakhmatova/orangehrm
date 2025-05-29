from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeavePage(BasePage):
    leave_tab = (By.LINK_TEXT, "Leave")
    apply_button = (By.LINK_TEXT, "Apply")
    from_date = (By.XPATH, "//input[@placeholder='From']")
    to_date = (By.XPATH, "//input[@placeholder='To']")
    comment = (By.XPATH, "//textarea")
    submit_btn = (By.XPATH, "//button[@type='submit']")

    def apply_leave(self, from_d, to_d, text):
        self.click(self.leave_tab)
        self.click(self.apply_button)
        self.fill(self.from_date, from_d)
        self.fill(self.to_date, to_d)
        self.fill(self.comment, text)
        self.click(self.submit_btn)
