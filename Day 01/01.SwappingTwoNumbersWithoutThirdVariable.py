#Swapping without using a temp variable

num1=10
num2=20

if num1 < num2 :
    
    print("In if - Before Swap",num1, num2)
    
    num2=num2+num1 #num2=30
    num1=num2-num1 #num1=20
    num2=num2-num1 #num2=10
    
    print("In if - After Swap",num1,num2)

else :

    print("In Else - Before Swap",num1, num2)

    num1=num1+num2
    num2=num1-num2
    num1=num1-num2

    print("In Else - After Swap",num1,num2)