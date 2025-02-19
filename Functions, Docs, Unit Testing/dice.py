# Program Name: dice.py
# Purpose: To roll dice and calculate their total
# Example Of: Functions for code reuse
from random import randint

def roll_dice():
    input("Press Enter to roll the dice ")
    roll1 = randint(1,6)
    roll2 = randint(1,6)
    total = roll1 + roll2
    print(f"You rolled: {roll1} and {roll2}, Total: {total}.")
    return total

# Call the function
# The code inside the if statement only runs if this script is executed, not imported
if __name__ == "__main__":
    print("Rolling 3 dice")
    roll(3)
    print()
    print("Rolling 2 dice")
    roll()

