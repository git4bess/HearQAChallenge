import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("chromeBrowserExecPath")
class TestSortTables(BaseClass):

    def test_sorttable(self, chromeBrowserExecPath):

        chromeDriver = webdriver.Chrome(executable_path=chromeBrowserExecPath[0])
        chromeDriver.get('https://the-internet.herokuapp.com/tables')
        log = self.getLogger()
        log.info("********** Test to sort tables has started **********")
        time.sleep(2)
        # Locate table1 and sort by last name ascending A..Z
        i = 0
        lastNameHeader = chromeDriver.find_element_by_css_selector('#table1 thead tr th:nth-child(1)')
        while lastNameHeader.get_attribute("class") != 'header headerSortDown':
            time.sleep(2)
            lastNameHeader.click()
            i += 1
            if i > 2:
                break

        print("Table 1 class is "+lastNameHeader.get_attribute("class"))
        # Locate table2 and sort by First name descending Z..A
        i = 0
        lastNameHeader = chromeDriver.find_element_by_css_selector('#table2 thead tr th:nth-child(2)')
        while lastNameHeader.get_attribute("class") != 'header headerSortUp':
            time.sleep(2)
            lastNameHeader.click()
            i += 1
            if i > 2:
                break

        time.sleep(10)
        chromeDriver.close()