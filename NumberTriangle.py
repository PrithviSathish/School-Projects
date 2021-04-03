n = int(input("Enter the value of n: "))

if n >= 2:
    print("Your output:- ")
    for i in range(1, 11):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

else:
    print("Please enter a higher value of n!")
