"""Euler 004 -
    Problem:
        A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
        Find the largest palindrome made from the product of two 3-digit numbers.
"""
lp = ([x, y, x * y] for x in range(100,1000) for y in range(100,1000) if x <= y and str(x * y) == str(x * y)[::-1])
result = [0,0,0]
poly = 0
for items in lp:
    if items[2] > result[2]:
        result = items
print(result)