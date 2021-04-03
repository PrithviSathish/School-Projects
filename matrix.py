# Matrix Project A

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
	for i in range(r1):
		for j in range(c1):
			if i == j or i + j == r1 - 1:
				print(A[i][j], end=' ')
			else:
				print(end= '  ')
		print()

else:
	print("Not possible")

print("Upper Triangle matrix")
if r1 == c1:
	for i in range(r1):
		for j in range(c1):
			if i <= j:
				print(A[i][j], end=' ')
			else:
				print(end='  ')

		print()

else:
	print("Not possible")


print("Sum of Column Elements")

for i in range(c1):
	s = 0
	for j in range(r1):
		s += A[j][i]
	print(s, end=' ')

print()

'''
for i in range(r1):
	for j in range(c1):
		print(A[i][j], end=' ')
	print()
print('---------')
'''


