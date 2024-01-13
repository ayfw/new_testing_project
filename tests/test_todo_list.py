from lib.todo_list import *

"""
initially incomplete list is empty
"""
def test_initial_incomplete_list():
    todo_list = TodoList()
    assert todo_list.incomplete() == []




"""
initially complete list is empty
"""
def test_initial_complete_list():
    todo_list = TodoList()
    assert todo_list.complete() == []


"""
when GIVEUP is called
marks all todo's as completed
"""
#def test_give_up_completes_all_todos():
#    todo_list = TodoList()
#    todo_list.add("task 1")
#    todo_list.add("task 2")
#    todo_list.give_up()
#    assert todo_list.complete() == ["task 1", "task 2"]