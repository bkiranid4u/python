"""
Problem:
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


def wordLen(num):

    d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    wordLength = 0

    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if num < 20:
        wordLength = len(d[num])
        return wordLength
    if num < 100:
        if(num % 10 == 0):
            wordLength = len(d[num])

        else:
            wordLength = len(d[(num//10) * 10]) + len(d[num % 10])
        return wordLength
    if num < k:
        if(num % 100 == 0):
            wordLength = len(d[num//100]) + len('hundred')
        else:
            wordLength = len(d[(num//100)]) + \
                len('hundredand') + wordLen(num % 100)
        return wordLength
    if num < m:
        #         if num % k == 0: return int_to_en(num // k) + ' thousand'
        #         else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)
        if(num % k == 0):
            wordLength = wordLen(num // k) + len('thousand')
        else:
            wordLength = wordLen(num // k) + \
                len('thousand') + wordLen(num % k)
        return wordLength


def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1


def countLetters(num):

    digitLenDict = (wordLen(i) for i in range(1, num+1))

    print(sum(digitLenDict))


countLetters(1000)
#  k = 1000
#     m = k * 1000
#     b = m * 1000
#     t = b * 1000

#     assert(0 <= num)

#     if (num < 20):
#         return d[num]

#     if (num < 100):
#         if num % 10 == 0: return d[num]
#         else: return d[num // 10 * 10] + '-' + d[num % 10]

#     if (num < k):
#         if num % 100 == 0: return d[num // 100] + ' hundred'
#         else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

#     if (num < m):
#         if num % k == 0: return int_to_en(num // k) + ' thousand'
#         else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

#     if (num < b):
#         if (num % m) == 0: return int_to_en(num // m) + ' million'
#         else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)
