# Collects number, makes list

def collectNumbers(totalNumbers):
        print("Please enter", totalNumbers, "numbers:")
        for i in range(0,totalNumbers):
            ele = float(input())
            myList.append(ele)

# Calculates average  

def calculateAverage():
    total = 0
    for i in range(0,len(myList)):
        total = total + myList[i]
    return (total/totalNumbers) 

myList = []

totalNumbers=int(input("Average of how many numbers? "))
collectNumbers(totalNumbers) # Calling function to create a list

average=calculateAverage()  # Calling function to calculate average
print("The average is : ", average)