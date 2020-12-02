def insertion_sort(theSeq):
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        print("Value Before While loop:", value)
        print("Position Before While loop:", pos)
        print("The sub list:", theSeq[i:])
        while pos > 0 and value < theSeq[i-1]:
            print("Position in While loop:", pos)
            theSeq[i] = theSeq[i-1]
            pos -= 1
        print(theSeq)
        print("Position After While loop:", pos)
        theSeq[pos] = value


print(insertion_sort([9, 8, 7, 4, 5, 6, 3, 2, 1]))
