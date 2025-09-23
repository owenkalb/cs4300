# Task3 test
import pytest
from task3 import check_number, first_10_primes, sum_1_to_100

# Test Pos, Neg, and Zero inputs
def test_check_number():
    assert check_number(1234) == "positive"
    assert check_number(-1234) == "negative"
    assert check_number(0) == "zero"

# Compare to see if first 10 are correct
def test_first_10_primes():
    assert first_10_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Does function also get 5050
def test_sum_1_to_100():
    assert sum_1_to_100() == 5050
    
