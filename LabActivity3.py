s1 = "Hello World Python"
s2 = ""
n = 0
for i in s1:
    n += 1
for j in range(n):
    if j == 0:
        if s1[i] >= 'A' and s1[i]<='Z':
            s2 += s1[i]
        else:
            x = ord(s1[i]) - 32
            s2 = chr(x)
    elif s1[i]=='':
        if s1[i + 1]>='A' and s1[i + 1] <= 'Z':
            s2 += s1[i + 1]

        else:
            x = ord(s1[i + 1]) - 32
            s2 += chr(x)

    else:
        s2 += s1[i]
print(s2)
