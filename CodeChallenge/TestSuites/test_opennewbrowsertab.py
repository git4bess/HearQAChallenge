import time

import pytest
from selenium import webdriver

from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("chromeBrowserExecPath")
class TestOpennewbrowsertab(BaseClass):
    def test_clickonnewtab(self, chromeBrowserExecPath):
        #logging that the test has started
        log = self.getLogger()
        log.info("*************  Open New browser test has started ************")
        chromeDriver = webdriver.Chrome(executable_path=chromeBrowserExecPath[0])
        chromeDriver.get("https://the-internet.herokuapp.com/windows")
        # Get the link and click on it
        chromeDriver.find_element_by_link_text("Click Here").click()
        # find new window and switch to it
        newtab = chromeDriver.window_handles[1]
        chromeDriver.switch_to.window(newtab)

        # locate text in new tab
        time.sleep(2)
        texttofind = chromeDriver.find_element_by_css_selector('div[class="example"] h3').text
        assert texttofind == "New Window"
        log.info("*************  Open New browser test has ended ************")
        chromeDriver.close()