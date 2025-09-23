import pytest
import task5

def test_first_three_books():
    expected = [
        ("Red Rising", "Pierce Brown"),
        ("Vicious", "V. E. Schwab"),
        ("Ender's Game", "Orson Scott Card")
    ]
    assert task5.first_three_books() == expected

def test_get_student_info_valid():
    # Should return correct ID for valid names
    assert task5.get_student_info("John") == "101"
    assert task5.get_student_info("Jill") == "103"
