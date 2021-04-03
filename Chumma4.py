n = int(input("Enter n: "))
x = int(input("Enter x: "))

Sum = 0
for i in range(0, n):
    factorial = 1
    for j in range(1, i * 3 + 2):
        factorial *= j
    Sum = Sum + 1 / factorial - ((i % 2) * 2 / factorial)

sum *= x
print(Sum)
