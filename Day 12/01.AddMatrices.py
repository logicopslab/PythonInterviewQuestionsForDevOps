# Program to add two matrices

M1 = [[10,100,230],
	[40,50,60],
	[70,80,90]]

M2 = [[90,100,70],
	[60,50,40],
	[30,20,10]]

M3 = [[0,0,0],
	[0,0,0],
	[0,0,0]]

# iterating rows

for i in range(len(M1)):

# iterating columns
	
	for j in range(len(M2)):
		M3[i][j] = M1[i][j] + M2[i][j]
		# print("i is", i, "j is", j)
		# print(M3)

print("Final Matrix is :")
for k in M3:
	print(k)
