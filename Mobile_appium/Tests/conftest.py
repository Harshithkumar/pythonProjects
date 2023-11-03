import appium.webdriver as wd
import pytest
import json

@pytest.fixture()
def setup():
    global driver
    f = open('/Users/hakumar/PycharmProjects/Experiments/Mobile_appium/Desired_caps/desired_cap.json')
    # returns JSON object as a dictionary
    des_cap = json.load(f)
    driver = wd.Remote("http://localhost:4723/wd/hub", des_cap)
    return driver


@pytest.fixture()
def tear_down_driver():
    yield
    driver.quit()
