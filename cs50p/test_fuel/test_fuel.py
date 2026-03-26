import pytest
from fuel import convert, gauge

def test_convert_invalid_value():
    # Test for X > Y (e.g., 6/5)
    with pytest.raises(ValueError):
        convert("6/5")

    # Test for X < 0 (e.g., -1/5)
    with pytest.raises(ValueError):
        convert("-1/5")

    # Test for non-integer input (e.g., cat/dog)
    with pytest.raises(ValueError):
        convert("cat/dog")

    # Test for incomplete fraction (e.g., 100)
    with pytest.raises(ValueError):
        convert("100")

def test_convert_zero_division():
    # Test for Y = 0 (e.g., 5/0)
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

#Test for convert() function to actual convert a str
def test_convert_valid_value():
    assert convert("5/6") == 83
    assert convert("2/4") == 50

#test for gauge() function labeling 1% as E
def test_gauge_empty():
    assert gauge(.5) == "E"
    assert gauge(1) == "E"
    assert gauge(.2) == "E"

#Test for guage() to be F
def test_guage_full():
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"
    assert gauge(99.7) == "F"

#Test for guage to print %
def test_guage_other():
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"


