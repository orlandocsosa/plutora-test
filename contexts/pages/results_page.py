from abstract_page import AbstractPage
from locators.search_results_locator import SearchResultsLocator
from selenium.webdriver.common.keys import Keys


class ResultsPage(AbstractPage):
    def get_results_count(self):
        elements = self.driver.find_elements(*SearchResultsLocator.RESULTS)
        return len(elements)