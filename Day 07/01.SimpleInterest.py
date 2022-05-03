# Simple Interest = (P x T x R)/100

def simpleInterest(principal,time,rate):
	print("The principal is : ", principal)
	print("The time period is : ", time)
	print("The rate of interest is : ",rate)
	
	return (principal * time * rate)/100
	
simple_interest = simpleInterest(3000, 7, 1)
print("The calculated Simple Interest is", simple_interest)