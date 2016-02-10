from abstract_context import AbstractContext
from pages.home_page import HomePage
from pages.results_page import ResultsPage


class TestSearch(AbstractContext):
    def test_search_main_page(self):
        hp = HomePage(self.driver)
        hp.go()
        hp.search_directly("test")
        rp = ResultsPage(self.driver)
        rp.wait(2)
        count = rp.get_results_count()
        assert count > 0

    def test_neg_search_main_page(self):
        hp = HomePage(self.driver)
        hp.go()
        hp.search_directly("negative testing :)")
        rp = ResultsPage(self.driver)
        rp.wait(2)
        count = rp.get_results_count()
        assert count == 0
