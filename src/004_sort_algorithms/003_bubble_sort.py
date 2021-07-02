
def bubble_sort(theSeq):

    n = len(theSeq)

    for i in range(n-1):

        for j in range(i, n-1):

            if theSeq[j] > theSeq[j+1]:
                theSeq[j], theSeq[j+1] = theSeq[j+1], theSeq[j]

    return theSeq


print(bubble_sort([1, 5, 64, 2, 5]))
