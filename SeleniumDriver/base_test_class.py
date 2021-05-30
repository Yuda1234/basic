import os
from ConfigTest.config import TestData
from SeleniumDriver.selenium_driver import Driver


class BaseTestClass:
    driver = None
    remove_logs_dir = False

    def setup(self):
        pass

    def setup_method(self, method):
        self.remove_logs_dir = False
        test_name = method.__name__
        self.init_driver()

    @staticmethod
    def get_base_url(default_url=TestData.BASE_URL):
        base_url = os.environ.get("BASE_URL", None)
        if base_url and "http" in base_url:
            return base_url
        else:
            return default_url

    def teardown_method(self):
        self.driver.driver.quit()

    def init_driver(self):
        self.driver = Driver(browser_profile="chrome")
        self.driver.driver.maximize_window()
        self.driver.driver.get(self.get_base_url())


