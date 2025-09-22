import pytest
from pytester import calculate_discount

def test_integer_inputs():
    assert calculate_discount(100, 20) == 80

def test_float_inputs():
    assert calculate_discount(150.0, 10.0) == 135.0

def test_mixed_inputs():
    assert calculate_discount(200, 25.5) == 149.0

def test_zero_discount():
    assert calculate_discount(50, 0) == 50

def test_full_discount():
    assert calculate_discount(80, 100) == 0

def test_invalid_type_price():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)

def test_invalid_type_discount():
    with pytest.raises(TypeError):
        calculate_discount(100, "10")

def test_negative_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, -5)

def test_discount_over_100():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)
