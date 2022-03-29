def primeOrNot(param):
    if(param==0):
        print ("The number is prime")
    else:
        print("The number is not prime")

num=float(input("Please enter the number : "))

if num > 0:
    primeOrNot(num)
else:
    print("Enter a valid number!")