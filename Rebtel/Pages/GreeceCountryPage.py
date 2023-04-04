from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.HomePage import HomeScreenPage
from Pages.Locators import Locators_page as loc
from Utils.custom_logger import Loggen


class GreecePage:
    screenshot_filepath = '/Users/hakumar/PycharmProjects/Experiments/Rebtel/Screenshots/'
    logger = Loggen()

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.HomeScreenPage_instance = HomeScreenPage(self.driver)

    def scroll_to_greece_cn(self):
        # pass the specific country element to click on that flag
        self.HomeScreenPage_instance.scroll_to_the_specific_country(country_flag=loc.LOC_GREECE_FLAG_XPATH,
                                                                    country_name=loc.LABEL_GREECE_CN_NAME)
        self.logger.info("Scrolled to the Page where Greece flag found !")

    def click_on_greece_flag(self):
        # Click on the Venezuela Image and verify all the parameter are correct or not
        if WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((MobileBy.XPATH, loc.LOC_GREECE_FLAG_XPATH))) \
                and loc.LABEL_GREECE_CN_NAME == self.driver.find_element_by_xpath(loc.LOC_GREECE_FLAG_XPATH).text:
            greece_flag = self.driver.find_element_by_xpath(loc.LOC_GREECE_FLAG_XPATH)
            greece_flag.click()
            self.logger.info("Greece flag element clicked")
            print("Greece flag element clicked")
        else:
            self.driver.save_screenshot(GreecePage.screenshot_filepath + 'Failed_GREECE_Flag.png')
            self.logger.critical("GREECE Flag element is not displayed or flag is missing")
            assert False, "GREECE Flag element is not displayed or flag is missing!!"

    def verify_greece_title(self):
        # Stale exception can be found here need to add try catch block
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        GREECE_TITLE = WebDriverWait(self.driver, 5, ignored_exceptions=ignored_exceptions) \
            .until(EC.presence_of_element_located((By.XPATH, loc.LOC_GREECE_TITLE)))
        if ignored_exceptions in (NoSuchElementException, StaleElementReferenceException):
            self.logger.critical("Not able to find the GREECE Flag info!. FAILED")
            self.driver.save_screenshot(GreecePage.screenshot_filepath + 'Failed_GRRECE_CN_INFO.png')


        GREECE_TITLE_TEXT = GREECE_TITLE.text
        print("GREECE TITLE is :", GREECE_TITLE_TEXT)
        if GREECE_TITLE_TEXT != loc.LABEL_GREECE_TITLE:
            self.driver.save_screenshot(GreecePage.screenshot_filepath + 'Failed_Greece_Title.png')
            self.logger.critical("GREECE TITLE mismatch. FAILED !")
            print("GREECE TITLE is : ", GREECE_TITLE_TEXT)
            assert False, "GREECE TITLE MISMATCH"

    def verify_greece_common_name(self):
        common_greece_name = self.driver.find_element_by_xpath(loc.LOC_GREECE_COMMON_NAME_VALUE_XPATH).text
        self.logger.critical("Verifying greece common name")
        print("Verifying greece common name")
        if common_greece_name != loc.LABEL_GREECE_COMMON_NAME:
            self.driver.save_screenshot(GreecePage.screenshot_filepath + 'Failed_Greece_common_name_error.png')
            self.logger.critical("Common name mismatch!! FAILED")
            assert False, "Common name mismatch!!"
