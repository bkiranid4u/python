"""
Problem: 21

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
"""


def sum_factors(num):
    result = []
    for i in range(1, int(num ** 0.5)):
        if num % i == 0:
            result.extend([i, num//i])
    return sum(set(result) - set([num]))


def amicable_pair(number):
    result = []
    for x in range(1, number+1):
        y = sum_factors(x)
        if sum_factors(y) == x and x != y:
            result.append(tuple(sorted((x, y))))

    print(sum([sum(x) for x in zip(*set(result))]))
    return set(result)


print(amicable_pair(10000))
