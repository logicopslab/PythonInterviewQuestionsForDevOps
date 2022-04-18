def reverseNumber(num):
    rev = 0
    while num!=0:
        rev = (rev * 10) + (num % 10)
        num = num // 10  # Floor division, 15/2 = 7.5 -> 7 

    return rev

num=int(input("Enter any number : "))
rev=reverseNumber(num)

if(rev==num):
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")