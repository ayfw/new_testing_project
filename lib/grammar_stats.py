class GrammarStats:
    def __init__(self):
        self._total_text = 0
        self._total_passed = 0
        
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self._total_text += 1
        if text == "":
            raise Exception ("This is empty!")
        elif text[0].isupper():
            self._total_passed += 1
            return text[-1] in ".?!"
        else:
            return False
        
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        # total_passed % total_all_text and then multiply by 100 to give percentage
        return (self._total_passed / self._total_text) * 100

  
   