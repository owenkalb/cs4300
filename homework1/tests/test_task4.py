# Task4 test
import pytest
from task4 import calculate_discount

# Int test
def test_integer_inputs():
    assert calculate_discount(100, 20) == 80

# Float test
def test_float_inputs():
    assert calculate_discount(150.0, 10.0) == 135.0

# Int & Float test
def test_mixed_inputs():
    assert calculate_discount(200, 25.5) == 149.0

# Zero
def test_zero_discount():
    assert calculate_discount(50, 0) == 50

# 100% off
def test_full_discount():
    assert calculate_discount(80, 100) == 0
