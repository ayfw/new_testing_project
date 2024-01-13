1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
"""
2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def task_tracker(text):
    """checks if text includes string #TODO

    Parameters: (list all parameters and their types)
        text: a string containing words and punctuation (e.g. "hello WORLD!")

    Returns: (state the return value and its type)
        a boolean, true if correct else false

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

"""
Given a text which includes #TODO
returns True
"""
task_checker("#TODO clean room") => True

"""
Given a text which includes TODO but no #
returns False
"""
task_checker("#TODO clean room") => False

"""
Given a text which does not include #TODO
returns False
"""
task_checker("I have already mopped the floors") => False

"""
Given an empty string
returns an error
"""
task_tracker("") => ["This is empty!"]



4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.task_tracker import *

"""
Given a text which does not include #TODO
returns False
"""
task_checker("I have already mopped the floors") => False

def test_includes_todo():
    result = task_tracker("#TODO clean room")
    assert result == True