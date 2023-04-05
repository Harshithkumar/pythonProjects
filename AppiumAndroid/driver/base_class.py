import logging
from datetime import datetime
from time import sleep
import os

import pytest
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait


class BaseMethods:

    screenshot_filepath = '/Users/hakumar/pythonProject/AppiumAndroid/Screenshots/'
    log_filepath = "/Users/hakumar/pythonProject/AppiumAndroid/Logs/app.log"

    def __init__(self, driver):
        self.driver = driver

    def is_visible(self, locator):
        if self.driver.find_element_by_id(locator).is_displayed():
            return True
        else:
            return False

    def find_element_by_id(self, locator):
        element_by_id = self.driver.find_element_by_id(locator)
        return element_by_id

    def click(self, locator):
        element = self.find_element_by_id(locator)
        element.click()

    def screenshot_on_failure(self, filename=''):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.save_screenshot(self.screenshot_filepath + f"{filename}_{now}.png")

    def get_logger(self):
        logging.basicConfig(filename=self.log_filepath)
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        ch = logging.FileHandler(r''f'{self.log_filepath}', mode='w')
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger