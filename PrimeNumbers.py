for i in range(1, 50):
    for j in range(2, i):
        if i % j ==0:
            # k = i / j
            print("Found a factor: ", i, "For ", j)
            break
    else:
        print(i, " Is a prime number")
