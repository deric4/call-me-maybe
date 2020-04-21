import pytest

def example_1(x: int, y: int) -> int:
    return x + y


def test_example_1a():
    assert example_1(1, 1) == 2
    assert example_1(2, 2) == 4
    assert example_1(3, 3) == 6


test_1_data = [
    (1,1,2),
    (2,2,4),
    (3,3,6),
]

@pytest.mark.parametrize("x,y,expected", test_1_data)
def test_example_1b(x, y, expected):
    """using parameterized values"""
    assert example_1(x, y) == expected


"Expecting a test to fail"

def example_2():
    return False

@pytest.mark.xfail(reason="Because it wants to")
def test_example_2a():
    assert example_2() == True

@pytest.mark.xfail(reason="Xfail but actually it passes")
def test_example_2b():
    assert example_2() == False

@pytest.mark.skip(reason="Skippy skip skip")
def test_example_2c():
    assert example_2 == False
