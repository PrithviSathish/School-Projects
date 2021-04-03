sum1 = sum2 = 0

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

sum1 = a + b + c

if a == b:
    if c != a:
        sum2 += c
else:
    if a == c:
        sum2 += b
    else:
        if b == c:
            sum2 += a
        else:
            sum2 += a + b + c

print("Sum of the numbers: ", sum1)
print("Sum of non-duplicated numbers: ", sum2)
