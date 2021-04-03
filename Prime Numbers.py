N = int(input("Enter the Value of n: "))
print("The prime numbers between 1 and ", N, "are:  ")


# Checks whether the number is a Prime Number or not
def PrimeNumbers(prime):
    for i in range(2, prime):
        if (prime % i) == 0:
            break
    else:
        print(prime)


# Main loop - calls the function
for j in range(1, N + 1):
    if j > 1:
        PrimeNumbers(j)
