import pytest
from tests.conftest import setup
from mobile.WTW_Page import Page_WTW_Screen


@pytest.mark.usefixtures('setup')
class BaseTests:

    @pytest.fixture
    def init(self):
        driver = self.driver
        self.my_WTW = Page_WTW_Screen(driver)
