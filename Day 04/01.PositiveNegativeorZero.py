
def positiveNegativeZero(param):
    if(param==0):
        print ("The number is either Zero or invalid")
    elif(param>0):
        print("The number is Positive")
    else:
        print("The number is Negative")

num=float(input("Please enter the number : "))

positiveNegativeZero(num) 