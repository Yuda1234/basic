from Pages.SomePage import SomePage
from Tests.base_project_test_class import *


class TestSomePage(BaseProjectTestClass):

    def test_google_page(self):
        self.driver.wait.wait_for_element_to_be_present(SomePage.LOGIN_NAV_BTN)
        self.driver.tools.wait_and_click(SomePage.LOGIN_NAV_BTN)



