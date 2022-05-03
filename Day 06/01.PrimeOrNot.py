def primeOrNot(param):
    for i in range(2, param):
        if((param%i)==0):
            print (param, "is not a prime number")
            break
    else:
        print(param, "is a prime number")

num=int(input("Please enter the number : "))

if num > 1:
    primeOrNot(num)
else:
    print("Enter a valid number!")

"""
for..else statement
This works on the logic that the else clause of the for loop runs if and only if we don't break out the for loop. 
That condition is met only when no factors are found, which means that the given number is prime.
So, in the else clause, we print that the number is prime.
"""