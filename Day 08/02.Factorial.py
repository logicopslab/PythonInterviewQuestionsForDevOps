def factorial(num):
    fact = 1
    while num!=0:
        fact = fact * num
        num -= 1
        # or num = num -1
    return fact

num=int(input("Enter any number : "))
print("The factorial of the number is :", factorial(num))