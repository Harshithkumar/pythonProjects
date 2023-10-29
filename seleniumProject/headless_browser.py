import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# instance of Options class allows
# us to configure Headless Chrome
options = Options()
URL = "https://qa3-platform.navigo.global/apps/router"
USERNAME = "automation@navigo-inc.com"
PASSWORD = "1234"

LocTxtUsername = (By.ID, "username")
LocTxtPassword = (By.ID, "password")
LocBtnLogin = (By.ID, "kc-login")
LOC_Air_Route_Drop_Down = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/select")

# this parameter tells Chrome that
# it should be run without UI (Headless)
options.add_argument('start-maximized')
options.add_experimental_option("detach", True)
# initializing webdriver for Chrome with our options
driver = webdriver.Chrome(options=options)


# getting GeekForGeeks webpage
driver.get(URL)
time.sleep(3)
driver.find_element(By.ID, 'username').send_keys(USERNAME)
driver.find_element(By.ID, 'password').send_keys(PASSWORD)
driver.find_element(By.ID, "kc-login").click()

time.sleep(7)
driver.find_element(By.XPATH, "//div[text()='Flight Schedules']").click()
time.sleep(4)
driver.find_element(By.XPATH, "//span[text()='Create New Flight Schedule']").click()
time.sleep(5)

#driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/select").click()
Element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(LOC_Air_Route_Drop_Down))
DropdownElement = Element
select = Select(DropdownElement)
options = select.options
for option in options:
    print(option.text)

select.select_by_visible_text("Brazil+auto123 (Brazil) - Suriname+auto789 (Suriname) [14:30 UTC to 19:30 UTC]")

