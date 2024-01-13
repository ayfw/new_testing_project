from lib.todo import *



"""
initialise todo and gets back todo
"""
def test_initialise_todo():
    todo = Todo("task 1")
    assert todo.task == "task 1"
    assert todo.complete == False


"""
mark task as complete
"""
def test_mark_task_complete():
    todo = Todo("task 1")
    todo.mark_complete()
    assert todo.complete == True