
from random import randint

def roll(num_dice=2):
    total = 0 # the total of the dice rolls

    # repeat until all the dice have been rolled
    for i in range(num_dice):
        number = randint(1,6)
        print("Rolled:", number)
        total += number ## add to the total

    print("Total", total)

    return total

# Call the function
# The code inside the if statement only runs if this script is executed, not imported
if __name__ == "__main__":
    print("Rolling 3 dice")
    roll(3)
    print()
    print("Rolling 2 dice")
    roll()

