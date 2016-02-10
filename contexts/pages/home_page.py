from abstract_page import AbstractPage
from locators.home_locator import HomeLocator
from selenium.webdriver.common.keys import Keys


class HomePage(AbstractPage):
    def click_search_button(self):
        element = self.driver.find_element(*HomeLocator.SEARCH_BUTTON)
        element.click()

    def enter_search_text(self, text):
        element = self.driver.find_element(*HomeLocator.SEARCH_INPUT)
        element.send_keys(text)

    def press_enter_on_search(self):
        element = self.driver.find_element(*HomeLocator.SEARCH_INPUT)
        element.send_keys(Keys.ENTER)

    def search_directly(self, text):
        self.click_search_button()
        self.enter_search_text(text)
        self.press_enter_on_search()

    def go(self):
        self.driver.get("http://www.plutora.com")
