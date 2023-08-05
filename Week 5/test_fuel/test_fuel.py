import pytest
from fuel import convert, gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("25/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("one/5")
        convert("7/two")
        convert("one/two")


def test_convert_input():
    assert convert("1/3") == 33
    assert convert("0/3") == 0
    assert convert("5/5") == 100


def test_gauge_res():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(45) == "45%"
