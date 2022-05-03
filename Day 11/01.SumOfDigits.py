def sumOfNum(myNumber):
    count = 0
    while(myNumber>0):
        myNumber = myNumber//10
        # print(myNumber)
        count = count + 1
    return count

myNumber = int(input("Please enter any number : "))

finalCount = sumOfNum(myNumber)

print("Total number of digits in the number is :", finalCount)

# Iteration 1
# 123 = 1234//10
# count 1
# Iteration 2
# 12 = 12//10
# count = 2
# Iteration 3
# 1 = 12//10
# count = 3
# You can calculate for 4 now