""" 
    HTML tag validator 
"""

from ArrayStack import ArrayStack


def htmlValidator(html):
    s = ArrayStack()
    j = html.find('<')
    while j != -1:
        # Opening tag is found 
        k = html.find('>',j+1)
        if k == -1:
            return False
        tag = html[j+1:k]
        if not tag.startswith('/'):
            s.push(tag)
        else:
            if s.is_empty():
                return False
            if tag[1:] != s.pop():
                return False
        j = html.find('<',k+1)
    return s.is_empty()
