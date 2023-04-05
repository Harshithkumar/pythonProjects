import logging

import pytest
from appium import webdriver


@pytest.fixture()
def setup(request):
    global driver
    capabilities = {
        "platformName": "android",
        "uuid": "RZ8N82K8STY",
        "deviceName": "Samsung Galaxy Note 20",
        "appPackage": "com.tivo.cableco",
        "appActivity": "com.tivo.android.screens.setup.SplashActivity",
        "noReset": True,
        "fullReset": False,
        "ignoreHiddenApiPolicyError": False,
        "newCommandTimeout": 1000,
        "enableMultiWindows": True
    }
    url = 'http://0.0.0.0:4723/wd/hub'
    request.instance.driver = webdriver.Remote(url, capabilities)
    request.instance.driver.implicitly_wait(20)

    def teardown():
        request.instance.driver.quit()
    request.addfinalizer(teardown)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = '/Users/hakumar/pythonProject/AppiumAndroid/report/report.html'
