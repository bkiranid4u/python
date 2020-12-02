def bubblesort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        for j in range(n-1):
            if theSeq[j] > theSeq[j+1]:
                temp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j+1] = temp
    return theSeq


print(bubblesort([9, 8, 7, 4, 5, 6, 3, 2, 1]))
