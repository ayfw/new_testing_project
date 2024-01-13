import pytest
from lib.grammar_checker import *

"""
Given sentence with a capital letter and fullstop
It returns True
"""
def test_grammar_check_uppercase_word_and_fullstop():
    result = grammar_checker("Hello there.")
    assert result == True

"""
Given sentence with a capital letter and no fullstop
It returns False
"""
def test_grammar_check_uppercase_word_no_fullstop():
    result = grammar_checker("Hello there")
    assert result == False

"""
Given sentence with no capital letter but a fullstop
It returns False
"""
def test_grammar_check_lowercase_word_and_fullstop():
    result = grammar_checker("hello there.")
    assert result == False

"""
Given a sentence starting with a lowercase word and no ending punction mark
returns False
"""
def test_grammar_check_lowercase_word_no_punct_mark():
    result = grammar_checker("hello there")
    assert result == False

"""
Given sentence with a capital letter and a exlamation mark
It returns True
"""
def test_grammar_check_uppercase_word_exclamation_mark():
    result = grammar_checker("Hello there!")
    assert result == True

"""
Given sentence with a capital letter and a question mark
It returns True
"""
def test_grammar_check_uppercase_word_question_mark():
    result = grammar_checker("Hello there?")
    assert result == True

"""
Given sentence with a capital letter and a comma
It returns False
"""
def test_grammar_check_uppercase_word_and_comma():
    result = grammar_checker("Hello there,")
    assert result == False

"""
Given an empty string
returns an error
"""
def test_grammar_check_empty_string():
    with pytest.raises(Exception) as e:
        grammar_checker("")
    error_message = str(e.value)
    assert error_message == "This is empty!"