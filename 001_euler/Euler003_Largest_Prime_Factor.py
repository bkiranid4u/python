"""Euler 003 -
    Problem:
        The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600851475143 ?
"""


def factors(n):
    p =2
    factors_list= []
    while n >= p*p:
        if n % p == 0:
            factors_list.append(p)
            n = n/p
        else:
            p = p +1
    factors_list.append(int(n))
    print(max(factors_list))
                
factors(600851475143)
