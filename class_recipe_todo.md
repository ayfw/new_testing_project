1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

"""
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks 
to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and 
have them disappear from the list.
"""

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class ToDo_List:
    def __init__(self):
    self._completed = completed
    self._incomplete = incomplete

    def add(self, text):
    a string representing a todo task
    returns a list with added tasks

    def remove(self, completed)
    given a completed task will then remove from the list
    returns a list with only incompleted tasks


3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
given a string without a #TODO
return an error
"""
def test_given_string_without_todo_raises_error():
    todo_list = ToDo_List()
    with pytest.raises(Exception) with e:
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
given a completed task
it will return list without the completed task
"""
def test_without_completed_task():
    todo_list = ToDo_List()
    result = todo_list.remove("#TODO clean room")
    assert result == [""]



4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.