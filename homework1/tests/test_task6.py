import pytest
from task6 import count_words_in_file

# Test that the word count function returns the expected number of words from the given file
def test_word_count_task6_read_me():
    file_path = 'task6_read_me.txt'
    expected_word_count = 104
    assert count_words_in_file(file_path) == expected_word_count

