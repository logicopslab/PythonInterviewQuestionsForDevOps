def concatString(input):
    result = ''
    for i in range(1,input+1):
        result = result + str(i)
    return result

input = int(input("Enter any digit : "))
print("Final String is :", concatString(input))