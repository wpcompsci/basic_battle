def room1():
	print("You have entered the first room...")
	nextRoom = input("Where would you like to go? (N, E): ")
	if nextRoom == "N":
		return 2
	elif nextRoom == "E":
		return 3

def room2():
	print("You have entered the north room...")
	nextRoom = input("Where would you like to go? (S): ")
	if nextRoom == "S":
		return 1

def room3():
	print("You have entered the east room...")
	nextRoom = input("Where would you like to go? (W, E): ")
	if nextRoom == "W":
		return 1
	elif nextRoom == "E":
		return 4
		
def room4():
	print("You have entered a room with a dragon...")
	print("He ate you. You are dead.")
	return 5
	
#### THE MAIN PROGRAM ####
room = 1

while True:
	if room == 1:
		room = room1()
	elif room == 2:
		room = room2()
	elif room == 3:
		room = room3()
	elif room == 4:
		room = room4()
	else:
		break

input("press enter to exit...")