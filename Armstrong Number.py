n = int(input("Enter n: "))
order = len(str(n))

Sum = 0
temp = n
while temp > 0:
    Digit = temp % 10
    Sum += Digit ** order
    temp //= 10

if n == Sum:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
