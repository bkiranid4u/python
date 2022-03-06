

from array import array


def max_element_recursive(s,n):

    if n == 1:
        # only one element
        return s[0]
    return max(s[n-1],max_element_recursive(s,n-1))

print(max_element_recursive([999,10,29,55,4444],5))

a=array[12]