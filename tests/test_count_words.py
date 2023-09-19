from lib.count_words import *

"""
if empty string given return 0
"""
def test_empty_string_given_return_zero():
    result = count_words("")
    assert result == 0

"""
if 1 word given return 1
"""
def test_one_string_given_return_one():
    result = count_words("hello")
    assert result == 1

"""
if 1 word with punctuation given return 1
"""
def test_one_string_punctuation_given_return_one():
    result = count_words("hello!")
    assert result == 1