"""
    Recursive Implementation of factorial function
"""


def factorial(n):

    # Base case to exit the recursive call - Structure
    if n == 0:
        return 1
    
    return n * factorial(n-1)


print(factorial(5))

