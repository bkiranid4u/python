""" 
    Matching the delimiters in a polynomial expression 
 """

from ArrayStack import ArrayStack


def matching_delimiters(expression):

    lefty = '({['
    righty = ')}]'

    s = ArrayStack()

    for char in expression:
        if char in lefty:
            # Opening of the delimiter. Push it to the stack
            s.push(char)
        if char in righty:
            if s.is_empty():
                return False
            if righty.index(char) != lefty.index(s.pop()):
                return False
    return s.is_empty()
