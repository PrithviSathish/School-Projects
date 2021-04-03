L = eval(input("Enter a list: "))
print("The original List is: ", L)
n = len(L)

print("Insert an element by position")

El = int(input("Enter element: "))
pos = int(input("Enter the position: "))

if pos <= n:
    L += [0]
    n = len(L)
    for i in range(n):
        if i == pos - 1:
            for j in range(n - 1, i, - 1):
                L[j] = L[j - 1]
            L[i] = El

    print("New list: ", L)
else:
    print("Enter a valid position")

print("Deleting Values")
print("Current list: ", L)
x = int(input("Enter the element: "))
for i in range(n):
    if L[i] == x:
        del L[i]
        print(x, "is deleted")
        break
