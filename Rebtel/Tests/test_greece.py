import allure
import pytest
from Pages.GreeceCountryPage import GreecePage
from Utils.custom_logger import Loggen


class Test_Greece(object):
    logger = Loggen()

    @pytest.mark.run  # we can also give xfail decorator if we know that specifc test case can fail.
    @allure.description("Verify GREECE Country info")
    @allure.severity(severity_level='CRITICAL')
    def test_greece_country_info(self, setup):  # we can pass teardown to driver to quit
        self.logger.info("**************** BEGIN of GREECE Country test ******************")
        self.driver = setup
        self.logger.info("Driver setup")

        self.greece_instance = GreecePage(self.driver)
        self.logger.info("Passing the driver instance to Brunie Page class")

        self.greece_instance.scroll_to_greece_cn()
        self.logger.info("Instantiating the object and calling Scrolling Page method to anchor GREECE CN")

        self.greece_instance.click_on_greece_flag()
        self.logger.info("Clicking on the Greece Flag")

        self.greece_instance.verify_greece_title()
        self.logger.info("Verifying Greece Title")

        self.greece_instance.verify_greece_common_name()
        self.logger.info("Verifying Greece Common name")
        self.logger.info("**************** End of GREECE Country test ******************")
