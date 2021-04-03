Number = int(input("Enter the Number: "))
First = 0
Second = 1
print(First)
print(Second)
for a in range(1, Number + 1):
    Third = First + Second
    print(Third)
    First, Second = Second, Third
