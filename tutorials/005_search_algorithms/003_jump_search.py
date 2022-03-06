""" 
    Jump Search

 """
from math import sqrt


class JumpSearch:

    def __init__(self) -> None:
        pass

    def search(self, arr, searchItem):

        # Finding block size to be jumped
        n = len(arr)
        step = sqrt(n)

        # Finding the block where element is
        # present (if it is present)
        prev = 0
        current = step
        while arr[int(min(current, n)-1)] < searchItem:
            prev = current
            current += step
            if prev >= n:
                return -1

        # Doing a linear search for x in
        # block beginning with prev.
        while arr[int(prev)] < searchItem:
            prev += 1

            # If we reached next block or end
            # of array, element is not present.
            if prev == min(step, n):
                return -1

        # If element is found
        if arr[int(prev)] == searchItem:
            return int(prev)

        return -1


jumpSearch = JumpSearch()
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
print(jumpSearch.search(arr, 144))
