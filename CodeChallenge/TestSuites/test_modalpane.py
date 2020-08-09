import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("chromeBrowserExecPath")
@pytest.mark.skip
class TestModalPane:

    def test_modalpane(self, chromeBrowserExecPath):
        chromeDriver = webdriver.Chrome(executable_path=chromeBrowserExecPath[0])
        chromeDriver.get('https://the-internet.herokuapp.com/exit_intent')
        chromeDriver.maximize_window()
        action = ActionChains(chromeDriver)
        time.sleep(5)
        element = chromeDriver.find_element_by_class_name("example")
        action.move_to_element(element).click().perform()
        time.sleep(5)
        # size = chromeDriver.get_window_size()
        action.move_by_offset(100, 200).perform()
        chromeDriver.close()