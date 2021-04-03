L = (2,3,4,5,6,2,3,4,5,2,3,4,3,2)
L2 = []
L3 = []
new = None
for i in L:
    num = 0
    if i not in L3:
        for j in L:
            if i == j:
                num += 1
        L3.append(i)
        L2.append(tuple((i,num)))

print(tuple(L2))

