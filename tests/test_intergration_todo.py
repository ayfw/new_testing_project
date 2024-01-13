from lib.todo import *
from lib.todo_list import *

"""
add a task to the todo list
"""
def test_add_task_todo_list():
    todo_list = TodoList()
    task_1 = Todo("clean room")
    assert todo_list.add(task_1) == [task_1]

"""
return list of incomplete tasks
"""
def test_return_list_of_incomplete():
    todo_list = TodoList()
    task_1 = Todo("clean room")
    task_2 = Todo("clean car")
    todo_list.add(task_1)
    todo_list.add(task_2)
    task_2.mark_complete()
    assert todo_list.incomplete() == [task_1]

"""
return list of complete tasks
"""
def test_return_list_of_complete():
    todo_list = TodoList()
    task_1 = Todo("clean room")
    task_2 = Todo("clean car")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.mark_complete()
    assert todo_list.incomplete() == []