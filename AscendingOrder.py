num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1 < num2:
    if num1 < num3:
        print(num1, end=" << ")
        if num2 < num3:
            print(num2, end=" << ")
            print(num3)
        else:
            print(num3, end= " << ")
            print(num2)
    else:
        print(num3, end=" << ")
        print(num1, end=" << ")
        print(num2)

else:
    if num2 < num3:
        print(num2, end=" << ")
        if num1 < num3:
            print(num1, end=" << ")
            print(num3)
        else:
            print(num3, end=" << ")
            print(num1)

    else:
        print(num3, end=" << ")
        print(num2, end=" << ")
        print(num1)

print()
