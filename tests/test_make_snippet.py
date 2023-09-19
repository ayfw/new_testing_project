from lib.make_snippet import *

"""
if empty string given return empty string
"""
def test_empty_string_return_empty_string():
    result = make_snippet("")
    assert result == ""

"""
if single word given return single word
"""
def test_single_word_given_return_single_word():
    result = make_snippet("hello")
    assert result == "hello"

"""
if 5 words given return 5 words
"""
def test_five_words_given_return_five_words():
    result = make_snippet("hello my name is Ben")
    assert result == "hello my name is Ben"

"""
if 6 words given return 5 words and ...
"""
def test_six_words_given_return_five_words_():
    result = make_snippet("hello my name is Ben Stone")
    assert result == "hello my name is Ben..."

