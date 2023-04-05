import pytest


from tests.base_tests import BaseTests


class Test_WTW(BaseTests):

    @pytest.mark.casticon
    def test_cast_icon(self, init):
        self.my_WTW.verify_cast_icon()

