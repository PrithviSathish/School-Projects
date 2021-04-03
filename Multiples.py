print("Enter 5 numbers: ")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))
num5 = int(input("Enter num5: "))

divisor = int(input("Enter the divisor: "))
count = 0

if num1 % divisor == 0:
    print("Num1 is a factor")
    count += 1

if num2 % divisor == 0:
    print("Num2 is a factor")
    count += 1

if num3 % divisor == 0:
    print("Num3 is a factor")
    count += 1

if num4 % divisor == 0:
    print("Num4 is a factor")
    count += 1

if num5 % divisor == 0:
    print("Num5 is a factor")
    count += 1

print()
print(count, "Multiples of", divisor, "are found")

