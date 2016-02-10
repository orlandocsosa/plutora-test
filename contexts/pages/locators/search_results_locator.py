from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class SearchResultsLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    RESULTS = (By.CLASS_NAME, "result")
