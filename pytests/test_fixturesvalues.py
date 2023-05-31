import pytest

@pytest.mark.skipif(False, reason="this fails")
def test_module_1(local_testing):
    assert 100 % local_testing == 0
    print('========this is test====')


@pytest.mark.order(2)  # inroder to excute , pytest-order package has been added a plugin.
def test_modular_2(local_testing):
    print("Order 2")
    assert 9 % local_testing == 9


@pytest.mark.order(1)
def test_modular_3(local_testing):
    print("Order 1")
    assert 5 * local_testing == 40
