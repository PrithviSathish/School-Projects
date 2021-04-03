L = [4, 5, 6, 8, 9, 3, 0]

for i in range(len(L)):
    if i < len(L)/2:
        first = L[i]
        L[i] = L[len(L) - (i + 1)]
        L[len(L) - (i + 1)] = first
    else:
        break

        
print(L)
