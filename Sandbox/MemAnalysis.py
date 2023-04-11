from datetime import time

from appium import webdriver
import hashlib
import fileinput
import plistlib
import pytest
import string


def getMemoryInfo(driver):
    pass


class Android_Memory():

    MEMORY_USAGE_WAIT= 30000
    MEMORY_CAPTURE_WAIT = 10;
    PKG = "io.appium.android.apis";
    PERF_TYPE = "memoryinfo";
    PSS_TYPE = "totalPss";

    @pytest
    def test_memory_usage():
        Desired_cap = {
            "platformName": "android",
            "uuid": "R52R405B0FH",
            "deviceName": "Samsung S7+",
            "appPackage": "com.tivo.cableco",
            "appActivity": "com.tivo.android.screens.setup.SplashActivity",
            "noReset": True,
            "newCommandTimeout": 500
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub",Desired_cap)
        try:
            # get the usage at one point in time
            totalPss1 = getMemoryInfo(driver).get(PSS_TYPE);

            #then get it again after waiting a while
            try:
                time.sleep(MEMORY_USAGE_WAIT);
            except:
                print("Excpetion")
            totalPss2 = getMemoryInfo(driver).get(PSS_TYPE)


