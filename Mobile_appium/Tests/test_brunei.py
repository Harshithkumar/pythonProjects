import allure
import pytest
from Pages.BruneiCountryPage import BruneiPage
from Utils.custom_logger import Loggen


class Test_Brunei(object):
    logger = Loggen()

    @pytest.mark.sanity(order=3)
    @allure.description("Verify BRUNIE Country info")
    @allure.severity(severity_level='MINOR')
    def test_brunei_country_info(self, setup):
        self.logger.info("**************** Begin of GREECE Country test ******************")

        self.driver = setup
        self.logger.info("Driver setup")

        self.bruniePage_instance = BruneiPage(self.driver)
        self.logger.info("Passing the driver instance to Brunie Page class")

        self.bruniePage_instance.scroll_to_brunei_cn()
        self.logger.info("Instantiating the object and calling Scrolling to BRUNEI CN")

        self.bruniePage_instance.verify_brunei_country_details()
        self.logger.info("Verifying the Country details")
        self.logger.info("**************** End of BRUNEI Country test ******************")