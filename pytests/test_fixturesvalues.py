import pytest

@pytest.mark.xfail
def test_module_1(local_testing):
    assert 100 % local_testing == 3
    print('========this is test====')

def test_module_2(local_testing):
    assert 9 % local_testing == 9
