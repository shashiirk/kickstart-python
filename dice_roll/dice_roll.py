from random import randint

def play():

    print("Press ENTER to roll and Q to quit.")
    roll = True

    while roll:
        x = input(":>")
        if len(x)==0:
            print(f"You rolled {randint(1,6)}")
        elif x.upper()=='Q':
            print("\nYou terminated the game...Bye!")
            roll = False
        else:
            print("Please enter a valid character!")

if __name__ == "__main__":
    play()