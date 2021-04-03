'''
Consider the List given below and write the python code(Without builtin and slicing)
	L=[6,2,5,8,1,9,6,3,6,4,2,9,2]

1.Create two Lists: one has numbers that are repeated more than once and another list with numbers that is present only once.(Both list should be unique) 

2. Count the no . of times each value present in a list as shown below
      6 - 3 time(s)
      2 - 3 time(s)
      5 - 1 time(s)
      ...........

3. Display the mode from the list.

4. Remove the specific element from the list and fill with zeros at the end whenever     deleting the element from list
       Original : [6,2,5,8,1,9,6,3,6,4,2,9,2]
             If 6 has to be removed
      Output : [2,5,8,1,9,3,4,2,9,2,0,0,0]
      (Note: Dont use additional List, changes should be done in the same list)
'''


L=[6,2,5,8,1,9,6,3,6,4,2,9,2]
print(L)
L1 = []
count = 0
n = []
# Number of times
for i in L:
	temp = count
	count = 0
	if i not in L1:
		L1.append(i)
		for j in L:
			if i == j:
				count += 1
			else:
				continue
		print(i, ":", count)
		if count > temp:
			n += [i]

	else:
		continue

print("Mode:", n)

rm = int(input("Enter the value to be removed: "))
num = 0
for i in L:
	if i == rm:
		L.remove(i)
		num += 1

for j in range(num):
	L += [0]

print(L)