import allure
import pytest
from Pages.HomePage import HomeScreenPage
from Utils.custom_logger import Loggen


class Test_HomeScreen_test:
    logger = Loggen()

    @pytest.mark.run(order=1)
    @allure.description("Verify HomePage Title")
    @allure.severity(severity_level='BLOCKER')
    def test_check_homescreen_title(self, setup):  # pass teardown to driver to quit
        self.logger.info("**************** Begin of HomePage Title test ******************")
        self.driver = setup
        self.logger.info("Driver setup")

        self.homePage_instance = HomeScreenPage(self.driver)
        self.logger.info("Creating the HomeScreenPage Object")

        self.homePage_instance.verify_title()
        self.logger.info("Verifying the HomePage Title")
        self.logger.info("**************** End of HomePage Title test ******************")
