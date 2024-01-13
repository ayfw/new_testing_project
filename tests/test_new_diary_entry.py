from lib.new_diary_entry import *

"""
initialise title and contents gets back title and contents
"""
def test_initialise_title_and_contents():
    diary_entry = DiaryEntry("my title 1", "my content 1")
    assert diary_entry.title == "my title 1"
    assert diary_entry.contents == "my content 1"

"""
count_words in the contents
"""
def test_counts_words_in_context():
    diary_entry = DiaryEntry("my title 1", "one two three")
    assert diary_entry.count_words() == 3

"""
calculate reading time
"""
def test_calculate_reading_time_returns_integer():
    diary_entry = DiaryEntry("my title 1", "one two three four five")
    assert diary_entry.reading_time(2) == 3

"""
given wpm and minutes
readable chunk returns chunks of the entries which are readable
and if called again returns the next readable chunk
"""
def test_readable_chunk_returns_chunks_of_entries():
    diary_entry = DiaryEntry("my title 1", "one two three four five")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"

"""
call the chunk again and should return final chunk
"""
def test_readable_chunk_returns_final_chunks_of_entries():
    diary_entry = DiaryEntry("my title 1", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1) 
    assert diary_entry.reading_chunk(2, 1) == "five"

"""
call the chunk again and should go back to the beginning
"""
def test_readable_chunk_returns_beginning_chunks_of_entries():
    diary_entry = DiaryEntry("my title 1", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1) 
    diary_entry.reading_chunk(2, 1) 
    assert diary_entry.reading_chunk(2, 1) == "one two"


