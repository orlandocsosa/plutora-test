from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class HomeLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    SEARCH_BUTTON = (By.ID, "search-btn")
    SEARCH_INPUT = (By.ID, "s")
    TYPEAHEAD_RESULTS = (By.CLASS_NAME, "ui-menu-item")


