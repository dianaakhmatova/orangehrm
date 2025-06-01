from selenium.webdriver.common.by import By

class BasePage:
    """
    Базовый класс для всех страниц. Содержит общие методы для работы с веб-элементами.
    """
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Открывает заданный URL."""
        self.driver.get(url)

    def find(self, locator):
        """Находит элемент по локатору."""
        return self.driver.find_element(*locator)

    def click(self, locator):
        """Кликает по элементу, найденному по локатору."""
        self.find(locator).click()

    def type(self, locator, text):
        """Вводит текст в поле, найденное по локатору."""
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(text)
