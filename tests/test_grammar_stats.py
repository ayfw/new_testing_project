import pytest
from lib.grammar_stats import *

"""
given an empty string
returns error
"""
def test_empty_string_error():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    error_message = str(e.value)
    assert error_message == "This is empty!"


"""
given string with capital letter and fullstop
return True
"""
def test_capital_letter_and_fullstop_true():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello there?")
    assert result == True

"""
given a text
return the percentage of the text that passes the check
"""
def test_percentage_of_text_check_passed():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello there?")
    grammar_stats.check("hello there")
    result = grammar_stats.percentage_good()
    assert result == 50