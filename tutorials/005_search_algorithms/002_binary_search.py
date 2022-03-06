"""  
Binary Search
"""


class BinarySearch:

    def __init__(self):

        pass

    def recursive_search(self, arr, startPos, endPos, searchItem):

        # Check base case
        if endPos >= startPos and endPos < len(arr):

            mid = startPos + (endPos - startPos) // 2

            # If element is present at the middle itself
            if arr[mid] == searchItem:
                return mid

            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif arr[mid] > searchItem:
                return self.recursive_search(arr, startPos, mid-1, searchItem)

            # Else the element can only be present
            # in right subarray
            else:
                return self.recursive_search(arr, mid + 1, endPos, searchItem)
        else:
            # Element is not present in the array

            return -1

    def iterative_search(self, arr, startPos, endPos, searchItem):
        while startPos <= endPos:
            middleIndex = startPos + (endPos - startPos) // 2
            if arr[middleIndex] == searchItem:
                return middleIndex
            elif arr[middleIndex] < searchItem:
                startPos = middleIndex + 1
            else:
                endPos = middleIndex - 1
        return -1


binarySearch = BinarySearch()
print(binarySearch.iterative_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 9))


# Driver Code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 9

# Function call
result = binarySearch.recursive_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
