import pytest
from src.main import divide


def test_div():
    result = divide(2, 2.0)
    assert 1 == result


def test_bad_args():
    with pytest.raises(Exception):
        divide("A", 1)


def test_zero_division():
    with pytest.raises(Exception):
        divide(1, 0)
