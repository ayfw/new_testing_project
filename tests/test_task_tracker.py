import pytest
from lib.task_tracker import *

"""
Given a text which includes #TODO
returns True
"""
def test_text_includes_todo_return_true():
    result = task_tracker("#TODO clean room")
    assert result == True

"""
Given a text which does not include #TODO
returns False
"""
def test_text_does_not_include_todo_return_false():
    result = task_tracker("clean room")
    assert result == False

"""
Given an empty string
returns an error
"""
def test_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        task_tracker("")
    error_message = str(e.value)
    assert error_message == "This is an empty string!"

"""
Given a text which includes TODO but no #
returns False
"""
def test_given_todo_but_no_hash():
    result = task_tracker("TODO clean room")
    assert result == False

