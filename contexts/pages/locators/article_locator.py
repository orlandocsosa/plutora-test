from abstract_locator import AbstractLocator
from abc import ABCMeta
from selenium.webdriver.common.by import By


class ArticleLocator(AbstractLocator):
    __metaclass__ = ABCMeta
    TITLE = (By.CLASS_NAME, "entry-title")
