import logging
from datetime import datetime
from time import sleep
import os

import pytest
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait


class BaseMethods:

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

    def screenshot_on_failure(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        new_file = self.driver.save_screenshot(f"screenshots_{now}.png")
        open(new_file)

    def get_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        ch = logging.FileHandler(r'logs/app.log', mode='w')
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger