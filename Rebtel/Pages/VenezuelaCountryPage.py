from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Locators import Locators_page as loc
from Utils.custom_logger import Loggen

class VenezuelaPage:
    logger = Loggen()
    screenshot_filepath = '/Users/hakumar/PycharmProjects/Experiments/Rebtel/Screenshots/'

    def __init__(self, driver):
        self.driver = driver

    def click_on_venez_flag(self):
        # Click on the Venezuela Image and verify all the parameter are correct or not
        if WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((MobileBy.XPATH, loc.LOC_VENEZ_XPATH))) \
                and loc.LABLE_VENEZ_CN_NAME == self.driver.find_element_by_xpath(loc.LOC_VENEZ_XPATH).text:
            venez_flag = self.driver.find_element_by_xpath(loc.LOC_VENEZ_XPATH)
            venez_flag.click()
            self.logger.info("Venezuela flag element clicked")
            print("Venezuela flag element clicked")
            assert True
        else:
            self.driver.save_screenshot(VenezuelaPage.screenshot_filepath + 'Failed_VENEZ_Flag.png')
            self.logger.critical("VENEZUELA Flag element is not displayed or flag is missing!!")
            assert False, "VENEZUELA Flag element is not displayed or flag is missing!!"

    def verify_venez_title(self):
        VENEZ_TITLE = self.driver.find_element_by_xpath(loc.LOC_VENEZ_TITLE_XPATH).text
        #print("Venezuela Coutntry title = ",VENEZ_TITLE)
        if VENEZ_TITLE != loc.LABEL_VENEZ_TITLE:
            self.driver.save_screenshot(VenezuelaPage.screenshot_filepath + 'Failed_Venezuela_Title.png')
            self.logger.critical("VENEZUELA TITLE Mismatch!!")
            print("Venezuela  Title is: ", VENEZ_TITLE)
            assert False, "VENEZUELA TITLE MISMATCH"
        else:
            self.logger.info("VENEZUELA TITLE PASSED")
            assert True

    def verify_venez_common_name(self):
        common_venez_name = self.driver.find_element_by_xpath(loc.LOC_VENEZ_COMMON_NAME_VALUE_XPATH).text
        self.logger.info("Verifying Venezuela common name")
        print("Verifying venezuela common name: ", common_venez_name)
        if common_venez_name != loc.LABEL_VENEZ_COMMON_NAME:
            self.driver.save_screenshot(VenezuelaPage.screenshot_filepath + 'Failed_venez_common_name_error.png')
            self.logger.critical("VENEZUELA Common Name Mismatch!!")
            print("venezuela common name is : ", common_venez_name)
            assert False, "Venezuela Common name mismatch!!"
        else:
            self.logger.info("VENEZUELA Common Name PASSED")
            assert True
