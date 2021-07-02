
arr = [64, 25, 12, 22, 11]


def selection_sort(theSeq):

    for i in range(0, len(theSeq)):
        minIndex = i
        for j in range(i+1, len(theSeq)):

            if theSeq[minIndex] > theSeq[j]:
                minIndex = j

        theSeq[i], theSeq[minIndex] = theSeq[minIndex], theSeq[i]

        print(theSeq)

    return theSeq


# print(selection_sort([64, 25, 12, 22, 22, 11]))
# print(selection_sort(['paper', 'true', 'soap', 'floppy', 'flower']))
# arr = ["GeeksforGeeks", "Practice.GeeksforGeeks", "GeeksQuiz"]
# print(selection_sort(arr))


def stableSelectionSort(a, n):

    # Traverse through all array elements
    for i in range(n):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j

        # Move minimum element at current i
        key = a[min_idx]
        # Shift the array right in the same order
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key


def printArray(a, n):
    for i in range(n):
        print("%d" % a[i], end=" ")


# Driver Code
a = [4, 5, 3, 2, 4, 1]
n = len(a)
stableSelectionSort(a, n)
printArray(a, n)
