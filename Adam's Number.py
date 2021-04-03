n = int(input("Enter n: "))  # gets the input from the user
sqr = n ** 2  # squares the value of n
t = n  # assigns value n to t
s = 0
while t != 0:  # loops until t becomes 0
    s = (s * 10) + (t % 10)  # gets the value of s
    t = t // 10

# Now s would be the reverse number of n

sqr2 = s ** 2  # square the value of s
p = sqr2  # Assign the value of the squared s to p
q = 0
# repeat the same loop
while p != 0:
    q = (q * 10) + (p % 10)
    p = p // 10

# check if the square of n is equal to the reverse of the square of s
if sqr == q:
    print("It is an Adam's number")
else:
    print("Sorry, the number is not an adam's number")
