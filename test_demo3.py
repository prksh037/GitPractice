import pytest

@pytest.mark.xfail
def test_math_div():
    a = 10
    b = 20
    assert a / b == 0.5, 'Division is not correct'
