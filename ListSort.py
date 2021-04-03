# Maximum and Minimum

n = int(input("Enter the value: "))
L = []
for i in range(n):
	print('Enter L[',i,']: ')
	L += [int(input())]


print("Original List: ", str(L))
L2, L3 = list(L), list(L)

ch = 0
while ch != 5:
	print("\n1. Maximum Value\n2. Minimum Value\n3. Ascending Order\n4. Descending Order\n5. Exit")
	ch = int(input("Enter your choice: "))

	if ch == 1:
		max = L[0]
		for i in range(1, n):
			if max < L[i]:
				print(i)
				max = L[i]
		print("Maximum Value: ", str(max))

	elif ch == 2:
		min = L[0]
		for i in range(1, n):
			if min > L[i]:
				min = L[i]
		print("Minimum Value: ", str(min))

	elif ch == 3:
		for i in range(n):
			t = i
			for j in range(i + 1, n):
				if L2[t] > L2[j]:
					t = j
			L2[i], L2[t] = L2[t], L2[i]
		print("Ascending order: ", str(L2))

	elif ch == 4:
		for i in range(n):
			for j in range(0, n - 1):
				if L2[j] < L2[j + 1]:
					L2[j], L2[j + 1] = L2[j + 1], L2[j]
		print("Descending Order: ", str(L2))

	elif ch == 5:
		print("Thank you!")
		break


