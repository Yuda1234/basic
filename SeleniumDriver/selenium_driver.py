from selenium import webdriver
from SeleniumDriver.ElementsTools.selenium_elements_tools import SeleniumElementsTools
from SeleniumDriver.wait_for_elements_tools import WaitForElementTools


class Driver:

    def __init__(self, browser_profile=None):

        if browser_profile == "chrome":
            self.driver = webdriver.Chrome()
            self.wait = WaitForElementTools(self.driver)
            self.tools = SeleniumElementsTools(self.driver, self.wait)

        elif browser_profile == "firefox":
            self.driver = webdriver.Firefox()
            self.wait = WaitForElementTools(self.driver)
            self.tools = SeleniumElementsTools(self.driver, self.wait)

