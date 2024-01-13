1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
"""
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
"""
2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def grammar_checker(text):
    """checks first word starts with capital letter and ends with a correct punctuation mark

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
Given a sentence starting with a lowercase word and no ending punction mark
returns False
"""
grammar_checker("hello there") => False

"""
Given sentence with a capital letter and fullstop
It returns True
"""
grammar_checker("Hello there.") => True

"""
Given sentence with a capital letter and no fullstop
It returns False
"""
grammar_checker("Hello there") => False

"""
Given sentence with no capital letter but a fullstop
It returns False
"""
grammar_checker("hello there.") => False

"""
Given sentence with a capital letter and a exlamation mark
It returns True
"""
grammar_checker("Hello there!") => True

"""
Given sentence with a capital letter and a question mark
It returns True
"""
grammar_checker("Hello there?") => True

"""
Given sentence with a capital letter and a comma
It returns False
"""
grammar_checker("Hello there,") => False

"""
Given an empty string
returns an error
"""
grammar_checker("") => ["This is empty!"]



4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.grammar_checker import *

"""
Given sentence with a capital letter and fullstop
It returns True
"""
def test_grammar_check_uppercase_word_and_fullstop():
    result = grammar_checker("Hello there.")
    assert result == True