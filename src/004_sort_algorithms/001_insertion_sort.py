"""Insertion Sort - Implementation

    Get value at i + 1 Position and start comparing the  sub array up to i th Position

"""


def insertion_sort(theSeq):
    # Check for empty array

    for i in range(1, len(theSeq)):

        value = theSeq[i]
        j = i - 1
        while j >= 0 and value < theSeq[j]:
            theSeq[j+1] = theSeq[j]
            j = j - 1
        theSeq[j + 1] = value

    return theSeq


# Test cases
print(insertion_sort([]))
print(insertion_sort([1]))
print(insertion_sort([1, 2]))
print(insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(insertion_sort([9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 7, 3, 8, 2, 9, 1]))


def insertion_sort_desc(theSeq):
    for i in range(1, len(theSeq)):
        value = theSeq[i]
        j = i-1
        while j >= 0 and value > theSeq[j]:
            theSeq[j+1] = theSeq[j]
            j = j - 1
        theSeq[j+1] = value
    return theSeq


print(insertion_sort_desc([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Test cases
print(insertion_sort_desc([]))
print(insertion_sort_desc([1]))
print(insertion_sort_desc([1, 2]))
print(insertion_sort_desc([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(insertion_sort_desc([9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(insertion_sort_desc(
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(insertion_sort_desc(
    [9, 1, 8, 2, 7, 3, 6, 4, 5, 5, 4, 6, 7, 3, 8, 2, 9, 1]))
