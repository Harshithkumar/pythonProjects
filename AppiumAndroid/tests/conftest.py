import os
import pytest
from driver import appium_driver
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()


@pytest.fixture()
def setup(request):
    appium_driver.start_appium_service()
    # appium_service.start(args=["-address", "localhost", "-p", "4723", "--base-path", ""])

    global driver
    capabilities = {
        "automationName": 'UiAutomator2',
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
    url = 'http://127.0.0.1:4723'
    request.instance.driver = webdriver.Remote(url, capabilities)
    request.instance.driver.start_activity('com.tivo.cableco', 'com.tivo.android.screens.setup.SplashActivity')
    request.instance.driver.implicitly_wait(20)

    def teardown():
        request.instance.driver.quit()
    request.addfinalizer(teardown)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = '/Users/hakumar/pythonProject/AppiumAndroid/report/report.html'
