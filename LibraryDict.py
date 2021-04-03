# Lab Activity 

d = {}
ch = 0
while ch != 6:
	print("\n1. Adding a book\n2. Displaying a book\n3. Updating quantity\n"
		"4. Deleting a book\n5. Display book\n6. Exit")
	ch = int(input("Enter your choice: "))

	if ch == 1:

		ISBN = int(input("Enter the ISBN number: "))

		# Check if ISBN is not present already
		if ISBN not in d.keys():

			# Getting value details
			book_name = input("Enter the book name: ")
			publish_name = input("Enter the publisher name: ")
			book_price = float(input("Enter the price: "))
			book_quantity = int(input("Enter the quantity of books: "))
			book_year = int(input("Enter the year: "))

			# Adding the book
			d[ISBN] = [book_name, publish_name, book_price, book_quantity, book_year] 
			print("New book added")

		else:
			print("Sorry, the book already exists!")

	elif ch == 2:

		# Check if ISBN number is present and search the book
		num = int(input("Enter the ISBN number: "))
		if num in d.keys():

			# Getting the values
			v = d[num]
			print("The book is: ", v[0])
			
		else:
			print("Book not available")

	elif ch == 3:
		num = int(input("Enter the ISBN number: "))
		if num in d.keys():
			d[num][3] += int(input("Enter the new quantity: "))
		else:
			print("Book info not available")

			
	elif ch == 4:
		num = int(input("Enter the ISBN number: "))
		if num in d.keys():
			del d[num]
		else:
			print("Book not added")

	elif ch == 5:
		print("\nISBN\tBook Name\tPublisher Name\t"
		"Book Price\tBook quantity \tBook year")

		for i in d.keys():
			x = d[i]
			print(i, end='\t')

			for j in x:
				print(j, end='\t')
			print()

	elif ch == 6:
		print("Thank you")
		break
