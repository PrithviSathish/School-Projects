L = [3, 5, 7, 9, 6, 0]
num = len(L)

for i in range(num - 1):
    for j in range(i + 1, num):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]

print(L)
