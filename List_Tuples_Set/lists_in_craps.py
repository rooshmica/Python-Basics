
from random import randint

print("===== Playing Craps =====")

# Make the first roll
input("Press Enter to roll the dice ")
roll1 = randint(1,6)
roll2 = randint(1,6)
total = roll1 + roll2
print(f"You rolled: {roll1} and {roll2}, Total: {total}.")

# Check if the player has won on the first roll
if total in [7,11]:
	print("You win")
	
# Check if the player has lost on the first roll
elif total in [2,3,12]:
	print("You lose")

# Otherwise we go to extra rolls
else:
	# Remember the player's first roll total as the "point"
	point = total
	total = 0
	print(f"Roll your point {point} to win, or 7 to lose.")

	# Keep rolling until player wins or loses
	while total not in [7,point]:
		input("Press Enter to roll the dice ")
		roll1 = randint(1,6)
		roll2 = randint(1,6)
		total = roll1 + roll2
		print(f"You rolled: {roll1} and {roll2}, Total: {total}.")


	# Game is over - did player win or lose?
	if total == 7:
		print("You lose")
	else:
		print("You win")

