# Gopal Lab project

n = int(input("Enter a Decimal: "))
d = n
L = []

while d != 0:
    rem = d % 2
    L.append(rem)

    d //= 2

print("Binary equallent: ", end=" ")
x = len(L) - 1
for i in range(x, -1, -1):
    print(L[i], end="")

d = n
L = []

while d != 0:
    rem = d % 8
    L.append(rem)

    d //= 8

print("\nOctal equallent: ", end=" ")
x = len(L) - 1
for i in range(x, -1, -1):
    print(L[i], end="")

d = n
L = []

while d != 0:
    rem = d % 16
    L.append(rem)

    d //= 16

print("\nHexadecimal equallent: ", end=" ")
x = len(L) - 1
for i in range(x, -1, -1):
    if L[i] == 10:
        print("A", end="")
    if L[i] == 11:
        print("B", end="")
    if L[i] == 12:
        print("C", end="")
    if L[i] == 13:
        print("D", end="")
    if L[i] == 14:
        print("E", end="")
    if L[i] == 15:
        print("F", end="")
    else:
        print(L[i], end="")

print()

