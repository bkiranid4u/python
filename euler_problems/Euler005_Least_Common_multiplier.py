"""Euler 005 -
    Problem:
        2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?.
"""
from math import gcd
def get_lcm(numbers):
    """ 
        product of two numbers is equal to product of lcm and gcd 
        Formula: n1 * n2 = lcm * gcd
        lcm = n1* n2 / gcd
    """
    lcm = numbers[0]

    for number in numbers[1:]:
        lcm = int(number * lcm /gcd(lcm,number))
    print(lcm)

get_lcm(list((i for i in range(1,21))))



