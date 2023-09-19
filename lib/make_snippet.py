"""
A function called make_snippet that takes a string as an argument 
and returns the first five words and then a '...' if there are more than that.
"""

def make_snippet(word):
    count_words = word.count(" ")+1
    five_words = ' '.join(word.split()[:5])
    if count_words > 5:
        return five_words + "..."
    else:
        return word
    