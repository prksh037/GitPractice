import pytest

def test_firstProgram():
    print('Hello')


def test_secondProgram():
    print('Hello again')


def test_math_mult():
    a = 10
    b = 20
    assert a * b == 200, 'Multipplication is not correct'

@pytest.mark.xfail
def test_math_div():
    a = 10
    b = 20
    assert a / b == 0.5, 'Division is not correct'
