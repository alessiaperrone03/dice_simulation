import random

def roll_dice(sides=6, rolls=1):
    results = []
    for _ in range(rolls):
        roll = random.randint(1, sides)
        results.append(roll)
    return results

def dice_simulation():
    print("Welcome to the Dice Simulation!")
    
    while True:
        # Ask the user how many sides the dice should have
        try:
            sides = int(input("Enter the number of sides for the dice (default is 6): ") or 6)
            if sides < 2:
                print("A dice must have at least 2 sides.")
                continue
        except ValueError:
            print("Please enter a valid number of sides.")
            continue
        
        # Ask the user how many times to roll the dice
        try:
            rolls = int(input("How many times would you like to roll the dice? (default is 1): ") or 1)
            if rolls < 1:
                print("You must roll the dice at least once.")
                continue
        except ValueError:
            print("Please enter a valid number of rolls.")
            continue
        
        # Roll the dice and display results
        results = roll_dice(sides, rolls)
        print(f"Results of {rolls} dice roll(s) with {sides}-sided dice: {results}")
        
        # Ask the user if they want to play again
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    dice_simulation()
