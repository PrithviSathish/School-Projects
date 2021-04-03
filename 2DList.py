print("Matrix-A")
r1 = int(input("Enter the number of rows: "))
c1 = int(input("Enter the number of columns: "))
A = [[0 for j in range(c1)] for i in range(r1)]

print("Enter the matrix for value A: ")
for i in range(r1):
	for j in range(c1):
		print('A[',i,']', '[',j,']')
		A[i][j] = int(input())


# Diagonal
print("Diagonal elements")
if r1 == c1:
	sum = 0
	for i in range(r1):
		for j in range(c1):
			if i == j or i + j == r1 - 1:
				print(A[i][j], end=' ')
				sum += A[i][j]
			else:
				print(end= '  ')
		print()

else:
	print("Not possible")

print("Sum: ", sum)

# Lower Left Triangle
print("Lower left Triangle")
if r1 == c1:
	for i in range(r1):
		for j in range(c1):
			if i >= j:
				print(A[i][j], end=' ')
			else:
				print(end = ' ')
		print()

else:
	print("Not possible")

# Interchanging digits
print("Interchanging digits")
if r1 == c1:
	for i in range(r1):
		for j in range(c1):
			if i != j and i < j:
				A[i][j], A[j][i] = A[j][i], A[i][j]

		print()

else:
	print("Not possible")

print("Interchanged value: ")
