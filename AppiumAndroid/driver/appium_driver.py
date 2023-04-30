import os
import subprocess
from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()


def start_appium_service():
    subprocess.Popen('appium', shell=True)



def stop_appium_service():
    appium_service.stop()
