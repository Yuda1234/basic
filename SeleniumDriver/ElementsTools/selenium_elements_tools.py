
class SeleniumElementsTools:

    def __init__(self, driver, wait_element):
        self.driver = driver
        self.wait = wait_element

    def wait_and_click(self, selector, driver=None, timeout=30, raise_exception=True):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_clickable(selector=selector, driver=driver, timeout=timeout,
                                                             raise_exception=raise_exception)
        if element:
            return element.click()

    def set_text(self, selector, text, driver=None, timeout=30):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout)
        element.send_keys(text)

    def get_text_from_element(self, selector, driver=None, timeout=30):
        driver = driver or self.driver
        element_text = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout).text
        return element_text

    def wait_and_get_element(self, selector, driver=None, timeout=30, raise_exception=True):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout,
                                                           raise_exception=raise_exception)
        if element:
            return element

