def primeOrNot(First, Second):
    for i in range (First, Second):
        if(First==0):
            print ("The number is prime")
        else:
            print("The number is not prime")

FirstInterval=float(input("Please enter the First interval : "))
SecondInterval=float(input("Please enter the Second interval : "))

if ((FirstInterval > 0 and SecondInterval > 0) and FirstInterval < SecondInterval):
    primeOrNot(FirstInterval, SecondInterval)
else:
    print("Enter a valid range!")