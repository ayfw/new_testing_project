"""
A function called count_words that takes a string as an argument and returns the number of words in that string.
"""

def count_words(text):
    word_count = len(text.split())
    return word_count