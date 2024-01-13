import pytest
from lib.diary_entry import *

"""
when given empty title and contents
return error
"""
def test_for_empty_title_and_content():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    assert str(e.value) == "Diary entry must have title or content"

"""
when given title and contents
return the title and contents
"""
def test_for_format():
    diary_entry = DiaryEntry("Harry Potter", "contents")
    result = diary_entry.format()
    assert result == "Harry Potter: contents"

"""
count words given in the diary entry
return an integer
"""
def test_count_words():
    diary_entry = DiaryEntry("Harry Potter", "contents")
    result = diary_entry.count_words()
    assert result == 3

"""
given the words per minute read then multiply by the amount of words
returns time taken to read those words
"""
def test_time_to_read_words():
    diary_entry = DiaryEntry("Harry Potter", "contents two three")
    result = diary_entry.reading_time(1)
    assert result == 3

"""
given 3 words of content and wpm of 2
return integer rounded up to equal here 2
"""
def test_time_to_read_words_rounded_up():
    diary_entry = DiaryEntry("Harry Potter", "contents two three")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
given wpm of 0
return error message
"""
def test_time_to_read_wpm_zero():
    diary_entry = DiaryEntry("Harry Potter", "contents two three")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "Reading time wpm is 0 can't calculate!"

"""
given content of 6 words
a wpm of 2
and a minute of 1
reading_chunk returns the first 2 words
"""
def test_reading_chunk_with_two_wpm_and_one_min():
    diary_entry = DiaryEntry("Harry Potter", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"

"""
given content of 6 words
a wpm of 4
and a minute of 1
reading_chunk returns the first 4 words
"""
def test_reading_chunk_with_four_wpm_and_one_min():
    diary_entry = DiaryEntry("Harry Potter", "one two three four five six")
    result = diary_entry.reading_chunk(4, 1)
    assert result == "one two three four"

"""
given content of 6 words
a wpm of 2
and a minute of 2
reading_chunk returns the first 4 words
"""
def test_reading_chunk_with_two_wpm_and_two_min():
    diary_entry = DiaryEntry("Harry Potter", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"

"""
given content of 6 words
a wpm of 2
and a minute of 1
First time reading_chunk returns "one two"
Next time return "three four"
Next time return "five six"
"""
def test_reading_chunk_with_two_wpm_and_one_min_call_multiple_times():
    diary_entry = DiaryEntry("Harry Potter", "one two three four five six")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"

"""
given content of 6 words
After read through all words should loop back to the beginning
"""
def test_reading_chunk_multiple_times_to_beginning():
    diary_entry = DiaryEntry("Harry Potter", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2, 1) == "one two"