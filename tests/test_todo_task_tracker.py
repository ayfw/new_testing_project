import pytest
from lib.todo_task_tracker import *

"""
given a string without a #TODO
return an error
"""
def test_given_string_without_todo_raises_error():
    todo_list = ToDo_List()
    with pytest.raises(Exception) as e:
        todo_list("")
        error_message = str(e.value)
        assert error_message == "No TODO given!"


"""
given a string with a #TODO
it will return list with the TODO added
"""
def test_given_a_todo_returns_list_with_todo():
    todo_list = ToDo_List()
    result = todo_list.add("#TODO clean room")
    assert result == ["#TODO clean room"]


"""
given a TODO task
it will remove the TODO task from the list
and it will change it to #COMPLETE
"""
def test_without_completed_task():
    todo_list = ToDo_List()
    todo_list.add("#TODO clean room")
    todo_list.add("#TODO clean house")
    todo_list.add("#TODO clean car")
    result = todo_list.remove("#TODO clean room")
    assert result == ["#TODO clean house", "#TODO clean car"]

"""
given a task without #TODO
it will not remove the task from the list
and it will not change it to #COMPLETE
it will raise an error

def test_given_no_todo_to_remove_raise_error():
    todo_list = ToDo_List()
    with pytest.raises(Exception) as e:
        todo_list.remove("TODO clean room")
        error_message = str(e.value)
        assert error_message == "Only #TODO tasks can be removed!"
"""
