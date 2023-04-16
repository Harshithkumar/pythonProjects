from driver.base_class import BaseMethods


class Page_WTW_Screen(BaseMethods):
    LOC_ID_CAST_ICON = "com.tivo.cableco:id/tivoCastButton"

    def verify_cast_icon(self):
        cast_icon_is_present = self.is_visible(self.LOC_ID_CAST_ICON)
        if cast_icon_is_present:
            self.click(self.LOC_ID_CAST_ICON)
            print("******YES ALL GOOD, PASSED!!")
            self.screenshot_on_failure(filename='passed_cast_icon')
            self.get_logger().info("******YES ALL GOOD, PASSED!!")
        else:
            self.screenshot_on_failure(filename='failed_cast_icon')
            self.get_logger().warning("******YES ALL GOOD, PASSED!!")
