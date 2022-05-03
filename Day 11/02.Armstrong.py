def checkArmstrong(myNumber):
	count = len(str(myNumber))
	temp = myNumber
	sum = 0
	while temp!=0:
		# getting last digit in the number
		lastDigit = temp%10
		# finding lastDigit ^ count
		sum = sum + (lastDigit**count)
		#floor division 
		#which update number with second last digit as last digit
		temp = temp//10 
	if sum==myNumber:
		print('Entered number is an Armstrong number')
	else:
		print('Entered number is not an Armstrong number')

myNumber = int(input("Please enter any number : "))
checkArmstrong(myNumber)