"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

# Read the file name

import string

fileName = "src/001_euler/Euler_Data/euler022_names.txt"

alphabet = string.ascii_uppercase


def alphabeticalScore(name):

    return sum([(alphabet.find(x) + 1) for x in name])


with open(fileName, "r") as file:
    total = 0
    array = []
    names = sorted(file.read().split(","))
    for name in names:
        total += alphabeticalScore(name) * (names.index(name)+1)

    print(total)
