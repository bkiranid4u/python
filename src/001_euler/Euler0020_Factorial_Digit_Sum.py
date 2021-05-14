"""
Problem: 
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
"""


def factorial(num):
    result = 1
    while num > 1:
        result = result * num
        num = num - 1

    return result


def recur_factorial(num):
    if num == 1:
        return num
    else:
        return num * recur_factorial(num-1)


print(sum([int(x) for x in str(recur_factorial(100))]))
