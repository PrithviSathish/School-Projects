'''
1
12
123
1234
12345
'''

Number = int(input("Enter the number: "))

for i in range(1, Number + 1):
    for j in range(1, i):
        print(j, end = ' ')
    print()
    

    
