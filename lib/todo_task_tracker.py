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

class ToDo_List:
    def __init__(self):
        self._list_of_todo = []
        

    def add(self, text):
        if text == "":
            raise Exception("No TODO given!")
        elif "#TODO" in text:
            self._list_of_todo.append(text)
            return self._list_of_todo
        
    def remove(self, text):
        #if "#TODO" not in text:
            #raise Exception("Only #TODO tasks can be removed")
        self._list_of_todo.remove(text)
        if "#TODO" in text:
            text.replace("#TODO", "#COMPLETED")
            return self._list_of_todo

        
        
    
        

            
        
