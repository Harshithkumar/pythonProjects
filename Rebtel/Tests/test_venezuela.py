import allure
import pytest
from Pages.VenezuelaCountryPage import VenezuelaPage
from Utils.custom_logger import Loggen


class Test_Venezuela(object):
    logger = Loggen()

    @pytest.mark.run(order=2)  # we can also give xfail decorator if we know that specifc test case can fail.
    @allure.description("Verify VENEZ Country info")
    @allure.severity(severity_level='NORMAL')
    def test_venez_country_info(self, setup):  # we can pass teardown to driver to quit
        self.logger.info("**************** BEGIN of VENEZ Country test ******************")
        self.driver = setup
        self.logger.info("Driver setup")

        self.venez_instance = VenezuelaPage(self.driver)
        self.logger.info("Created the VenzePage Object")

        self.venez_instance.click_on_venez_flag()
        self.logger.info("clicked on the Venez flag")

        self.venez_instance.verify_venez_title()
        self.logger.info("Verifing on the Venez Title")

        self.venez_instance.verify_venez_common_name()
        self.logger.info("Verifying on the Venez common name")
        self.logger.info("**************** End of VENEZ Country test ******************")
