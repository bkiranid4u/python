"""Euler 002 -
    Problem:
        Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
        By starting with 1 and 2, the first 10 terms will be:
        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
        By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
        find the sum of the even-valued terms.
"""
# generator expression approach 

def even_fib(n):
    a = 0
    b = 1
    while a < n:
        yield a
        a, b = b, a+b

print(sum(list((x for x in even_fib(4000000) if x % 2 == 0))))
