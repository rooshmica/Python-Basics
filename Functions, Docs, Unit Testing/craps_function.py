# Program Name: section05_example01b_craps_function.py
# Purpose: To play the Craps Dice Game
# Example Of: Function roll_dice to avoid Code duplication
from random import randint

def roll_dice():
    input("Press Enter to roll the dice ")
    roll1 = randint(1,6)
    roll2 = randint(1,6)
    total = roll1 + roll2
    print(f"You rolled: {roll1} and {roll2}, Total: {total}.")
    return total

amount = 100
play_again = "yes"

while play_again == "yes":
    print()
    print("===== Playing Craps =====")    
    print(f"You have {amount}")
    # Input the player"s bet and subtract it from the amount
    bet = int(input("Enter your bet: "))
    amount -= bet

    # Make the first roll
    total = roll_dice()

    # Check if the player has won on the first roll
    if total == 7 or total == 11:
        print("You win")
        amount += bet * 2
        
    # Check if the player has lost on the first roll
    elif total == 2 or total == 3 or total == 12:
        print("You lose")

    # Otherwise we go to extra rolls
    else:
        # Remember the player's first roll total as the "point"
        point = total
        total = 0
        print(f"Roll your point {point} to win, or 7 to lose.")

        # Keep rolling until player wins or loses
        while total != 7 and total != point:
            total = roll_dice()

        # Game is over - did player win or lose?
        if total == 7:
            print("You lose")
            
            if amount <= 0:
                print("You're broke!")
                break
        else:
            print("You win")
            amount += bet * 2

    print(f"You now have {amount}")
    play_again = input("Play again? ")

print("Game over!")
