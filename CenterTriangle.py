"""
                1
              121
            12321
          1234321
        123454321
      12345654321

"""

Number = int(input("Enter the number: "))
for i in range(1, Number + 1):
    for k in range(i, Number):
        print(end="  ")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
