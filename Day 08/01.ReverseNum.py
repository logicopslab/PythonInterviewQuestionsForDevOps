def reverseNumber(num):
    rev = 0
    while num!=0:
        rev = (rev * 10) + (num % 10)
        num = num // 10  # Floor division, 15/2 = 7.5 -> 7 

    return rev

num=int(input("Enter any number : "))
print("The reversed number is :", reverseNumber(num))