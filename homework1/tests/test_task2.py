# Task2 test
import pytest
import task2

#Test that each variable in task2 has the expected type
def test_variable_types():
    assert isinstance(task2.a, int), "a should be an int"
    assert isinstance(task2.b, float), "b should be a float"
    assert isinstance(task2.c, str), "c should be a string"
    assert isinstance(task2.d, bool), "d should be a bool"


def test_variable_values():
    assert task2.a == 10
    assert task2.b == 1.234
    assert task2.c == "string"
    assert task2.d is True
