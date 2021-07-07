"""
Recursive Implementation of binary Search
"""


def binary_search(list, searchItem, startIndex, endIndex):

    if startIndex > endIndex:
        return False

    mid = (startIndex + endIndex)//2

    if list[mid] == searchItem:
        return True

    if list[mid] < searchItem:
        binary_search(list, searchItem, mid+1, endIndex)

    if list[mid] > searchItem:
        binary_search(list, searchItem, startIndex, mid-1)


def binary_search_iterative(list, searchitem, start, end):

    if start > end:
        return False

    while start > end:
        mid = (start + end) // 2

        if list[mid] == searchitem:
            return True
        elif list[mid] > searchitem:
            end = mid - 1
        else:
            start = mid + 1

    return False
