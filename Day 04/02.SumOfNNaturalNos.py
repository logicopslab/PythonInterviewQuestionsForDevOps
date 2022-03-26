# Formula -> n (n+1) / 2

def sumOfNNaturalNos(param):
    result = param * ( param + 1 )
    result = result / 2
    return result
    
    # return (param * (param+1) / 2)

num=float(input("Please enter the number : "))

if (num > 0):
    print("The sum of N natural number is :",sumOfNNaturalNos(num)) 
else:
    print("Enter a valid number!")    