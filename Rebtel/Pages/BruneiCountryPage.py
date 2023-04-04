from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.HomePage import HomeScreenPage
from Pages.Locators import Locators_page as loc
from Utils.custom_logger import Loggen


class BruneiPage:
    screenshot_filepath = '/Users/hakumar/PycharmProjects/Experiments/Rebtel/Screenshots/'
    logger = Loggen()

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.HomeScreenPage_instance = HomeScreenPage(self.driver)

    def scroll_to_brunei_cn(self):
        # pass the specific country element to click on that flag
        if not self.HomeScreenPage_instance.scroll_to_the_specific_country(country_flag=loc.LOC_BRUNEI_FLAG_XPATH,
                                                                    country_name=loc.LABEL_BRUNEI_CN_NAME):
            assert False, "County not found"
        else:
            self.driver.save_screenshot(BruneiPage.screenshot_filepath + 'Failed_BRUNIE_CN_NOT_FOUND.png')
            self.logger.info("Scrolled to the Page where Brunie flag found !")
            pass

    def verify_brunei_country_details(self):
        if self.driver.find_element_by_xpath(loc.LOC_BRUNEI_FLAG_XPATH).is_displayed():
            self.driver.find_element_by_xpath(loc.LOC_BRUNEI_FLAG_XPATH).click()
            self.logger.info("clickng on the the flag to open the cn info")
            print("clickng on the the flag to open the cn info")
        else:
            self.driver.save_screenshot(BruneiPage.screenshot_filepath + 'Failed_BRUNIE_CN_NOT_DISPLAYED.png')
            self.logger.critical("Not able to open the BRUNIE Flag !. FAILED")
            assert False

        # handle the StaleElement exception
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        BRUNEI_TITLE = WebDriverWait(self.driver, 5, ignored_exceptions=ignored_exceptions) \
            .until(EC.presence_of_element_located((By.XPATH, loc.LOC_BRUNEI_TITLE)))
        if ignored_exceptions in (NoSuchElementException, StaleElementReferenceException):
            self.logger.critical("Not able to find the BRUNIE Flag info!. FAILED")
            self.driver.save_screenshot(BruneiPage.screenshot_filepath + 'Failed_BRUNIE_CN_INFO.png')

        # get the info for country title, common name, region
        TITLE_TEXT = BRUNEI_TITLE.text
        COMMON_NAME_TEXT = self.driver.find_element_by_xpath(loc.LOC_BRUNEI_COMMON_NAME).text
        REGION_TEXT = self.driver.find_element_by_xpath(loc.LOC_BRUNEI_REGION).text
        print("BRUNEI TITLE NAME = ", TITLE_TEXT)
        print("BRUNEI COMMON NAME = ", COMMON_NAME_TEXT)
        print("BRUNEI REGION NAME = ", REGION_TEXT)

        # if any on info is failed, take the screenshot and assert it as a false
        if (loc.LABEL_BRUNEI_TITLE_NAME != TITLE_TEXT) and (loc.LABEL_BRUNEI_COMMON_NAME == COMMON_NAME_TEXT) \
                and (loc.LABEL_BRUNEI_REGION == REGION_TEXT):
            self.logger.critical("Brunei country information mismatch ! FAILED")
            self.driver.save_screenshot(BruneiPage.screenshot_filepath + 'Failed_BRUNIE_CN_INFO.png')
            assert False, "Brunei country information mismatch !!"
        else:
            self.logger.info("Brunei country information matched ! PASSED")
            assert True
