""" 
Problem 14
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# from itertools import count

# maxChainLength = 0
# for number in count(1, 1):
#     if number > 0 and number <= 1000000:
#         sequence = number
#         chainLength = 1
#         while sequence != 1:

#             if sequence % 2 == 0:
#                 sequence = sequence/2

#             else:
#                 sequence = 3 * sequence + 1

#             chainLength += 1

#         if chainLength > maxChainLength:
#             maxChainLength = chainLength
#     else:
#         break
# print(maxChainLength)

# With caching


def main(n):
    list = [1, 2]
    for i in range(3, n):
        count = 0
        while i > len(list):
            if i % 2 == 0:
                i = i/2
            else:
                i = 3*i+1
            count += 1
        list.append(count + list[int(i)-1])
    return list.index(max(list))+1


print(main(1000001))
