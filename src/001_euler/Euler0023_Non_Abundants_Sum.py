"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from math import sqrt


def abundant_number(num):

    divisors = []
    for i in range(1, int(num ** 0.5) + 1):

        if num % i == 0:
            divisors.extend([i, num // i])

    divisors.remove(num)
    if sum(set(divisors)) > num:
        return True


abundant_nos = [x for x in range(1, 28123 + 1) if abundant_number(x)]
k = 0
abundantList = []
for i in abundant_nos:
    for j in abundant_nos[k:]:
        if(i+j > 28123):
            break
        abundantList.append(i+j)
        # num_list[i+j-1] = False
    k += 1

print(sum(range(1, 28124)) - sum(set(abundantList)))
