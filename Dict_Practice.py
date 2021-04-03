# Lab Activity

'''
players = {"Kedar Jadav":{"Country":"India", "Matches":350; "Runs": 10773; "Avg":50.58},
			"Virat Kohli":{"Country":"India", "Matches":251; "Runs": 12040; "Avg":59.31},
			"Babar Azam":{"Country":"Pakistan", "Matches":77; "Runs": 3580; "Avg":55.94},
			"Steve Smith":{"Country":"Australia", "Matches":128; "Runs": 4378; "Avg":43.35},
			"Kane Williamson":{"Country":"New Zealand", "Matches":151; "Runs": 6174; "Avg":47.49}}
'''
player = {}
ch = 0

while ch != 6:
	print("\n1. Add\n2. Search\n3. Update\n4. Delete\n5. Display All\n")
	ch = int(input("Enter your choice: "))

	if ch == 1:

		name = input("Enter the player name: ")

		# Checking whether the player exists and adding the details into the dictonary
		if name not in player.keys():
			Country = input("Enter the Country of the player: ")
			Matches = int(input("Enter the number of Matches: "))
			Runs = int(input("Enter the total runs scored by the player: "))
			Avg = float(input("Enter the batting average of the player: "))

			player[name] = [Country, Matches, Runs, Avg]
		else:
			print("Name already exists")

	elif ch == 2:

		name = input("Enter the player name: ")

		if name in player.keys():
			print("Country: ", list(player.values())[0][0])
			print("Matches: ", list(player.values())[0][1])
			print("Runs: ", list(player.values())[0][2])
			print("Avg: ", list(player.values())[0][3])
		else:
			print("Player not found")

	elif ch == 3:

		name = input("Enter the player name: ")

		if name in player.keys():
			runs = int(input("Enter the runs scored: "))
			list(player.values())[0][2] += runs
			print("Player details updated")
		else:
			print("Player not found")

	elif ch == 4:

		name = input("Enter the player name: ")

		if name in player.keys():
			del player[name]
			print("Player deleted")
		else:
			print("Player not found")

	elif ch == 5:
		print("\nPlayer Name\tCountry\tMatches played\t"
		"Runs scored\tBatting average")

		for i in player.keys():
			x = player[i]
			print(i, end='\t')

			for j in x:
				print(j, end='\t')
			print()

	elif ch == 6:
		print("Thank you")

