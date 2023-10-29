import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chromium.options import ChromiumOptions as Options

url = "https://www.youtube.com/"


def get_webdriver(context):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


def get_screenshot(context):
    current_date_time = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
    screenshot_path = os.path.join(os.path.abspath('Selenium/LearnIt'),
                                   f"Failed_Screenshots_{current_date_time}.png")
    context.driver.save_screenshot("test.png")


get_webdriver()
get_screenshot()
