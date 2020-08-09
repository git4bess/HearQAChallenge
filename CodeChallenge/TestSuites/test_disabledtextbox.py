import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("chromeBrowserExecPath")
class TestDisabledtextbox(BaseClass):

    def test_disabledtext(self, chromeBrowserExecPath):
        chromeDriver = webdriver.Chrome(executable_path=chromeBrowserExecPath[0])
        chromeDriver.get('https://the-internet.herokuapp.com/dynamic_controls')
        chromeDriver.maximize_window()
        log = self.getLogger()
        log.info("********** Test with Dynamic controls has started **********")

        time.sleep(2)
        # Find the button to enable the textbox
        btn = chromeDriver.find_element_by_css_selector('#input-example button')
        btn.click()
        textbox = WebDriverWait(chromeDriver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input")))
        textbox.send_keys("The text is enabled")


        #Disable the textbox and check for the value
        btn.click()
        WebDriverWait(chromeDriver, 10).until(EC.text_to_be_present_in_element((By.ID,"message"),"It's disabled!"))
        assert ((EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,"#input-example input"),"the text is enabled")) is not None) == True
        chromeDriver.close()