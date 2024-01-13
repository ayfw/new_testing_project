def grammar_checker(text):
    if text == "":
        raise Exception ("This is empty!")
    elif text[0].isupper():
        return text[-1] in ".?!"
    else:
        return False
    
    
