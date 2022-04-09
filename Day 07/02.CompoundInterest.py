# a, p, r, t
# A = P (1+R/100) raise to the power t

def compInt(principal,rate,time):
    amount = principal * (pow(1 + (rate/100), time))
    return amount - principal

principal=float(input("Please enter the Principal : "))
rate=float(input("Please enter the Rate : "))
time=float(input("Please enter the Time : "))

print("The Compound Interest is :", compInt(principal,rate,time))