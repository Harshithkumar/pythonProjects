import pytest

import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# instance of Options class allows
# us to configure Headless Chrome

options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)


def open_browser():
    URL = "https://qa3-platform.navigo.global/apps/router"
    USERNAME = "automation@navigo-inc.com"
    PASSWORD = "1234"
    # LocTxtUsername = (By.ID, "username")
    # LocTxtPassword = (By.ID, "password")
    # LocBtnLogin = (By.ID, "kc-login")
    print("Driver Initialized")
    driver.get(URL)
    print("Opening Navigo URL")
    time.sleep(3)
    driver.find_element(By.ID, 'username').send_keys(USERNAME)
    print("Entering Username")
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)
    print("Entering Password")
    driver.find_element(By.ID, "kc-login").click()
    print("Submit btn clicked")
    flight_tab()


def flight_tab():
    LOC_Air_Route_Drop_Down = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/select")

    # this parameter tells Chrome that
    # it should be run without UI (Headless)
    # options.add_argument('start-maximized')
    # options.add_experimental_option("detach", True)
    # initializing webdriver for Chrome with our options

    time.sleep(7)
    driver.find_element(By.XPATH, "//div[text()='Flight Schedules']").click()
    print("clicked on TAB")
    time.sleep(4)
    driver.find_element(By.XPATH, "//span[text()='Create New Flight Schedule']").click()
    print("Clicked on Create New Btn")
    time.sleep(5)
    print("Waiting to load the Flight Schedules from dropdown")
    Element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(LOC_Air_Route_Drop_Down))
    DropdownElement = Element
    select = Select(DropdownElement)
    s_options = select.options
    SelectedOption = random.choice(s_options)
    SelectedChoice = SelectedOption.text
    select.select_by_visible_text(SelectedChoice)
    print("print selcted choice from the dropdown: ", SelectedChoice)
    # if select.select_by_visible_text("Brazil+auto123 (Brazil) - Suriname+auto789 (Suriname) [14:30 UTC to 19:30 UTC]"):
    #     print("Dropdown selected")
    # else:
    #     print("Error")
