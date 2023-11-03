from Pages.Locators import Locators_page as loc
from Utils.custom_logger import Loggen


class HomeScreenPage(object):
    screenshot_filepath = '/Users/hakumar/PycharmProjects/Experiments/Mobile_appium/Screenshots/'
    repeat = 21
    logger = Loggen()

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def verify_title(self):
        # Verify that title is proper or not
        TITLE_TEXT = self.driver.find_element_by_xpath(loc.LOC_HOMETITLE_XPATH).text
        self.logger.info("Verifying the homepage Title")
        print("Verifying Title: ", TITLE_TEXT)

        # If the title doesn't match then it will take the screenshot in PNG format
        if loc.LABEL_TEXT_TITLE != TITLE_TEXT:
            self.logger.critical("Home Title Mismatch. FAILED")
            self.driver.save_screenshot(HomeScreenPage.screenshot_filepath + 'Failed_title.png')
        else:
            self.driver.save_screenshot(HomeScreenPage.screenshot_filepath + 'Passed_title.png')
            self.logger.info("Home Title Matched. PASSED")
            assert loc.LABEL_TEXT_TITLE == TITLE_TEXT, "Title mismatch"

    def get_position_to_scroll(self):
        # This func is to get the start of x,y and end of x,y position to begin scrolling
        start_x = self.driver.find_element_by_xpath(loc.LOC_FROM_BOTTOM).location['x']
        start_y = self.driver.find_element_by_xpath(loc.LOC_FROM_BOTTOM).location['y']
        # start_x = 545
        # start_y = 2245
        self.logger.info("Getting Scrolling position of Start X and Y")
        print(f'Scrolling from {start_x} and {start_y}  location')

        end_x = self.driver.find_element_by_xpath(loc.LOC_TO_TOP).location['x']
        end_y = self.driver.find_element_by_xpath(loc.LOC_TO_TOP).location['y']
        # end_x = 545
        # end_y = 332
        self.logger.info("Getting Scrolling position of END X and Y")
        print(f'Scrolling to {end_x} and {end_y} location values')
        return start_x, start_y, end_x, end_y

    def scroll_to_end_of_the_screen(self):
        # This func is to scroll the page to till end of the screen.
        s_x, s_y, e_x, e_y = self.get_position_to_scroll()
        c = 0
        self.logger.info("Scrolling the Page till end")
        for i in range(self.repeat):
            if self.driver.find_element_by_xpath(loc.LOC_VISIBLE_FLAG_ON_EACH_SCROLL).is_displayed():
                c = c + 1
                self.driver.swipe(s_x, s_y, e_x, e_y, 2000)
            else:
                self.driver.save_screenshot(HomeScreenPage.screenshot_filepath + 'Scrolling_failed.png')
        print(f'Scrolled {c} times')

    def scroll_to_the_specific_country(self, country_flag=None, country_name=None):
        # This func is to scroll the page to till specified country found.
        s_x, s_y, e_x, e_y = self.get_position_to_scroll()
        c = 0
        self.logger.info("Scrolling the Page till specific element is found")
        for i in range(self.repeat):
            if self.driver.find_element_by_xpath(loc.LOC_VISIBLE_FLAG_ON_EACH_SCROLL).is_displayed():
                c = c + 1
                # scroll to required country
                if country_name == self.driver.find_element_by_xpath(country_flag).text:
                    # self.driver.find_element_by_xpath(country_flag).click()
                    print("Country name is : ", self.driver.find_element_by_xpath(country_flag).text)
                    break
                self.driver.flick(s_x, s_y, e_x, e_y)
            else:
                self.driver.save_screenshot(HomeScreenPage.screenshot_filepath + 'Scrolling_req_cn_failed.png')
                print(f'Scrolled {c} times')
                return False

    def scroll_to_find_each_flag(self, country_name=None):
        cn_names = []
        for m in range(2,13):
            self.driver.implicitly_wait(5)
            temp = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                                     "android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/"
                                                     "android.view.View/android.view.View/android.view.View/"
                                                     "android.view.View[2]/android.view.View[{}]/android.view.View".format(m)).text

            if country_name == temp:
                print("Selected country ===== ", temp)
                break
        print(cn_names)
