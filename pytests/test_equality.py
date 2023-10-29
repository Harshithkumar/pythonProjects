import pytest


@pytest.fixture
def test_equality():
    # with pytest.raises(AssertionError) as e:
    assert 100 == 200


@pytest.mark.usefixtures('test_less')
def test_greater_equal():
    num = 200
    print("This test is to check which is greater and it is passed !")
    assert num < 100


@pytest.fixture()
def test_less():
    num = 100
    assert num < 200
    print("\n This line prints only if asserts PASS or else it wont print")


def test_module_3(local_testing):
    assert 9 * local_testing == 90
