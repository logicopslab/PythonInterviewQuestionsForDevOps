def countOccurrance(myChar, myString):

    count = 0
    for i in range(len(myString)):
        if(myString[i] == myChar):
            count = count + 1
    return count

myString = input("Please enter String : ")
myChar = input("Please enter a Character : ")
count = countOccurrance(myChar, myString)

print("Total number of occurences of", myChar, "is :" , count)
