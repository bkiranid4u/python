from array import Array

def countChars() :
    theCounter = Array( 127 )
    theCounter.clear(  0)
    theFile = open("/Users/kirankumar/GitHub/python/testData/numchar.txt")
    for line in theFile:
        for letter in line:
            code = ord( letter )
            theCounter[code] +=1
    theFile.close()
    for i in range( 26 ):
        print("%c  - %4d         %c - %4d"%(chr( 65 + i ), theCounter[ 65 + i], chr(97 + i), theCounter[ 97 + i]))
countChars()
