def selection_sort(theList):
    n = len(theList)

    for i in range(n-1):
        small_index = i
        for j in range(i+1, n-1):
            if theList[j] < theList[small_index]:
                small_index = j

        if i != small_index:
            temp = theList[i]
            theList[i] = theList[small_index]
            theList[small_index] = temp
