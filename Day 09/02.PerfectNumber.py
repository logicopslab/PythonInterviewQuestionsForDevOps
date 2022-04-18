num = int(input("Enter a number : "))
sum=0
for i in range (1, (num // 2) + 1):
    rem = num % i
    if rem == 0:
        sum = sum + i
if sum == num:
    print("Yes, it is a Perfect number")
else:
    print("No, it is not a perfect number") 