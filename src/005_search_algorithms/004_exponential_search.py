""" 
Exponential Search
 """


class ExponentialSearch:

    def __init__(self) -> None:
        pass

    def binarySearch(self, arr, startPos, endPos, searchItem):

        if endPos >= startPos and endPos < len(arr):

            mid = int(startPos + (endPos - 1) // 2)

            if arr[mid] == searchItem:
                return mid
            elif arr[mid] > searchItem:
                return self.binarySearch(arr, startPos, mid-1, searchItem)

            return self.binarySearch(arr, mid+1, endPos, searchItem)

        return -1

    def expSearch(self, arr, searchItem):

        if arr[0] == searchItem:
            return 0
        i = 1
        length = len(arr)
        while i < length and arr[i] <= searchItem:
            i = i * 2
        print(i)
        return self.binarySearch(arr, i/2, int(min(i, length - 1)), searchItem)


arr = [2, 3, 4, 10, 40]
exponentialSearch = ExponentialSearch()
result = exponentialSearch.expSearch(arr, 10)
if result == -1:
    print("Element not found in thye array")
else:
    print("Element is present at index %d" % (result))
