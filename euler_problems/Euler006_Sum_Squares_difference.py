"""Euler 005 -
    Problem:
        The sum of the squares of the first ten natural numbers is,

pow(1,2) + pow(2,2) + ... + pow(10,2) = 385
The square of the sum of the first ten natural numbers is,

pow((1 + 2 + ... + 10),2) = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from math import gcd
def get_sum_square_diff(n):
    """
        Formulaes: 
            Sum of the squares of the first N natural numbers = n(n+1)(2n+1)/6
            Square of the sume of first n natural numbers = pow(n(n+1)/2),2) 
    """
    diff = int(pow((n * (n+1)/2),2) - (n*(n+1)*(2*n+1)/6))
    print(diff)

get_sum_square_diff(100)