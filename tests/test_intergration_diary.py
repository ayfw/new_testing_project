from lib.diary import *
from lib.new_diary_entry import *

"""
add a diary entry to the diary list
"""
def test_add_entry_to_diary():
    diary = Diary()
    entry_1 = DiaryEntry("my title 1", "my contents 1")
    diary.add(entry_1)
    assert diary.all() == [entry_1]

"""
add multiple diary entries to the diary list
returns a list of all entries
"""
def test_add_entries_to_diary_return_list_of_all():
    diary = Diary()
    entry_1 = DiaryEntry("my title 1", "my contents 1")
    entry_2 = DiaryEntry("my title 2", "my contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]


"""
given I add 2 entries
I use count_words to count total sum of words in the contents part of the entries
"""
def test_given_two_entries_count_words_in_contents():
    diary = Diary()
    entry_1 = DiaryEntry("my title 1", "my contents 1")
    entry_2 = DiaryEntry("my title 2", "my contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 6

"""
given 2 diary entries total length of 5
with a wpm of 2
should return 2.5 -> 3
"""
def test_calculate_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry("my title 1", "one two")
    diary.add(entry_1)
    entry_2 = DiaryEntry("my title 2", "three four five")
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

"""
given 2 diary entries, one is short and one is long
wpm is 2 and minutes to read is 2 = 4 words you can read
returns the diary which fits that condition
"""
def test_find_best_entry_to_read():
    diary = Diary()
    entry_1 = DiaryEntry("my title 1", "one two three")
    entry_2 = DiaryEntry("my title 2", "one two three four five six")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 2) == entry_1

"""
if reading ability can't read any of the entries
returns None
"""
def test_reading_ability_cannot_read_entries():
    diary = Diary()
    entry_1 = DiaryEntry("my title 1", "one two three")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(1, 2) == None
   