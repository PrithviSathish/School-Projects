import math

ch = 0
while ch != 5:
    print("Find the area of:  \n 1. Square \n 2. Rectangle \n 3. Triangle \n 4. Circle \n 5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        side = int(input("Enter the length of a side: "))
        print("Area of the square =", str(side ** 2))

    elif ch == 2:
        length = int(input("Enter the length: "))
        breadth = int(input("Enter the breadth: "))
        print("Area of the square =", str(length * breadth))

    elif ch == 3:
        base = int(input("Enter the length of the base: "))
        height = int(input("Enter the height: "))
        print("Area of the triangle=", str((base * height) / 2))

    elif ch == 4:
        radius = int(input("Enter the radius: "))
        print("Area of the circle=", str(math.pi * (radius ** 2)))

print("Thank you!")
