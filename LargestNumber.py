x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))

if x > y and x > z:
    print("x is the greatest number")
elif y > x and y > z:
    print("Y is the greatest number")
else:
    print("z is the greatest number")
