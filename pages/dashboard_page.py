from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.dashboard_header = (By.TAG_NAME, "h6")

    def is_dashboard_displayed(self):
        return "Dashboard" in self.driver.find_element(*self.dashboard_header).text