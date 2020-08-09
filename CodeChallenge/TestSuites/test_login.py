# This is crazy
import time
import pytest

import selenium
from selenium import webdriver
# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


#class test_login(BaseClass):
@pytest.mark.usefixtures("setup")
class Testlogin(BaseClass):

    def test_loginwithvalidcredentials(self):

        time.sleep(5)
        log = self.getLogger()
        log.info("********** Login test with Valid credentials has started **********")

        # find the textboxes, enter the values and click on the button
        self.driver.find_element_by_id('username').send_keys('tomsmith')
        self.driver.find_element_by_id('password').send_keys('SuperSecretPassword!')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
        # verify that the user is redirected to a new page and that the successful login message is displayed
        time.sleep(5)
        pageUrl = self.driver.current_url
        messageDisplayed = self.driver.find_element_by_id("flash").text
        assert pageUrl == 'https://the-internet.herokuapp.com/secure', 'User is not redirected to the Secure area'
        #assert messageDisplayed == 'You logged into a secure area!', 'Successful message is not displayed'
        assert 'You logged into a secure area' in messageDisplayed, 'Successful message not displayed'

    @pytest.mark.usefixtures("logindata")
    def test_loginwithInvalidCredentials(self,logindata):
        log = self.getLogger()
        log.info("********** Login test with invalid credentials has started **********")
        time.sleep(5)
        #clear all text
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('password').clear()

        #pick all data
        if logindata[0] != "":
            self.driver.find_element_by_id('username').send_keys(logindata[0])
        if logindata[1] != "":
            self.driver.find_element_by_id('password').send_keys(logindata[1])

        self.driver.find_element_by_css_selector('button[type="submit"').click()
        # verify that the user is redirected to a new page and that the successful login message is displayed
        #time.sleep(5)
        flashmessage = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "flash")))
        #transfer message in messageDisplayed
        messageDisplayed = flashmessage.text
        assert logindata[2] in messageDisplayed, "Invalid message not displayed"
