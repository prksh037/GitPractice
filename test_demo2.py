import pytest

@pytest.mark.skip
def test_secondProgram():
    msg = 'Hello'
    assert msg == 'Hi', 'Hello & Hi are different'

@pytest.mark.run
def test_math_add():
    a = 10
    b = 20
    assert a + b == 30, 'Addition is not correct'


def test_math_sub():
    a = 10
    b = 20
    assert b-a == 10, 'Subtraction is not correct'


