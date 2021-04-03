ch = 0
while ch != 6:
    print("\n1. Length \n2. Copy\n3. Concat\n4. Reverse\n5. Equal\nExit")
    ch = int(input("Enter ch: "))
    if ch == 1:
        s1 = input("Enter the string: ")
        x = 0
        for i in s1:
            x += 1
        print("String length: ", x)

    elif ch == 2:
        s1 = input("Enter the string: ")
        s2 = s1
        print("String copied from s1 to s2: ", s2)

    elif ch == 3:
        s1 = input("Enter the String: ")
        s2 = input("Enter the String2: ")
        s2 = s1 + s2
        print("Concatenated string: ", s2)

    elif ch == 4:
        s1 = input("Enter the string: ")
        x = 0
        for i in s1:
            x += 1
        s2 = ""
        for i in range(x - 1, - 1, -1):
            s2 += s1[i]
        print("Reversed string: ", s2)

    elif ch == 5:
        s1 = input("Enter string1: ")
        s2 = input("Enter string2: ")
        if s1 == s2:
            print("Strings are equal")
        else:
            print("Strings are not equal")

    elif ch == 6:
        print("Thank you")

    else:
        print("Please enter a valid choice")
