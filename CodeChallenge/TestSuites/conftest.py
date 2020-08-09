import pathlib
from pathlib import Path

import pytest
from selenium import webdriver

# from selenium.webdriver.support.select import Select


@pytest.fixture()
def setup(request):
    base_path = Path.cwd()
    file_path = base_path.parent
    driver_path = file_path.as_posix() + "/Utilities/allDrivers/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path)
    #driver = webdriver.Chrome(executable_path="/home/sonitakooh/Downloads/allDrivers/chromedriver")
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(params=[("", "", "Your username is invalid"), ("tom", "mess!72", "Your username is invalid"), ("paul", "SuperSecretPassword!", "Your username is invalid"), ("tomsmith", "mypassword", "Your password is invalid")])
def logindata(request):
    return request.param

@pytest.fixture()
def chromeBrowserExecPath():

    base_path = Path.cwd()
    base_path = base_path.parent
    driver_path = base_path.as_posix() + "/Utilities/allDrivers/chromedriver"
    return [str(driver_path)]
