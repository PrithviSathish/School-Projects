Number = int(input("Enter the number:  "))
Num1, Num2 = -5, 10
for i in range(1, Number + 1):
    print(Num1, Num2)
    Num1, Num2 = Num1 - 10, Num2 + 10
