import random
def roll_dice():
    return random.randint(1,6)
print("Dice rolling simulator")
while True:
     roll = input("roll the dice?(yes/no):")
     if roll == "yes":
        print("You rolled:",roll_dice())
     elif roll == "no":
        print("Thanks for playing!")
        break
     else:
        print("please type 'yes' or 'no'")

