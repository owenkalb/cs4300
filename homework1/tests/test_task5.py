import pytest
import task5

# Check if 1-3 books are correct
def test_first_three_books():
    expected = [
        ("Red Rising", "Pierce Brown"),
        ("Vicious", "V. E. Schwab"),
        ("Ender's Game", "Orson Scott Card")
    ]
    assert task5.first_three_books() == expected

# Should return correct ID for valid names
def test_get_student_info_valid():
    assert task5.get_student_info("John") == "101"
    assert task5.get_student_info("Jill") == "103"
