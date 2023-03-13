import pytest


@pytest.mark.interger
def test_one_plus_one():
    assert 5 + 5 == 10


# ==========================================

@pytest.mark.interger
def test_one_minus_one():
    assert 5 - 5 == 0


# ===========================================

@pytest.mark.zero
def test_zero_div():
    with pytest.raises(ZeroDivisionError) as e:
        num = 2 / 0
        assert 'divison by 100' in str(e.value)


# ---------
# Parameterzised function
# ---------


Products = [
    (2, 3, 6),  # +ve integers
    (1, 99, 99),  # Identity verification
    (0, 99, 0),  # Zero validation
    (3, -4, -12),  # +ve by _ve multiply
    (-5, -5, 25),  # -ve by -ve multiple
    (2.5, 2.5, 6.25),  # flaoting multiply
]


@pytest.mark.production
@pytest.mark.parametrize('a, b, product', Products)
def test_multilpication(a, b, product):
    assert a * b == product
# =====================================
