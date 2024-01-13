import pytest
from lib.diary import *

"""
initially given empty list
"""
def test_initial_empty_list():
    diary = Diary()
    assert diary.all() == []

"""
initially word count is 0
"""
def test_initial_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0

"""
initially reading time is 0 and raises error
"""
def test_initially_reading_time_raise_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(2)
    error_message = str(e.value)
    assert error_message == "there are no entries!"
