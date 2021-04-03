Number = int(input("Enter the number: "))
Sum = 0
for i in range(1, Number + 1):
    if i == 1:
        Sum = 1
        # print(Sum)
    else:
        Sum = i * Sum
        # print(Sum)

print(Sum)
