"""Euler 005 -
    Problem:
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
        What is the 10 001st prime number?
"""
from math import sqrt
def is_prime_number(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i  <= sqrt(n):
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6
    return True

def get_10001_prime_number():
    count = 0
    i =2
    while count < 10001:
        if is_prime_number(i):
            count += 1
        i +=1
    print(i-1)
    

get_10001_prime_number()