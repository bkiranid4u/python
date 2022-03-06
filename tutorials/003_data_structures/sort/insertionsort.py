def insertion_sort(theSeq):
    n = len(theSeq)
    # No need to check for length of the sequence as the range function - doesn't return the sequence if the length is less than 2
    for i in range(1, n):
        value = theSeq[i]
        pos = i - 1
        while pos > 0 and value > theSeq[i-1]:
            theSeq[i] = theSeq[i-1]
            pos -= 1
        theSeq[pos] = value
    return theSeq


print(insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])
