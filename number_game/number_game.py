import random

def get_key():
    
    try:
        n = int(input("Enter the key: "))
    except Exception as e:
        print(e)
        return get_key()
    else:
        return n

def continue_or_not():
    
    c = input("\nDo you want to play again (Y|N)? ")
    if c.upper()=='Y':
        return True
    elif c.upper()=='N':
        return False
    else:
        print("Please enter a valid character!")
        return continue_or_not()

def play():

    games_played = 0
    games_won = 0
    print(f"\n{7*'='} NUMBER GUESSING GAME {7*'='}")
    print("Guess the correct key[1-10] to win.")

    while True:
        games_played += 1
        key = random.randrange(1,10)
        chances = 3
        guesses = []
        
        while chances != 0:
            print(f"\nPrevious Guesses: {' '.join(map(str, guesses))}")
            print(f"Chances Left: {chances}")
            
            n = get_key()
            
            if(n == key):
                print("\nCongrats!.You won the Game.")
                games_won += 1
                break
            else:
                if(n in guesses):
                    print("You already guessed this number!")
                    chances += 1
                else:
                    guesses.append(n)
                    if(n<key):
                        print("Incorrect!.Key is Bigger than you guessed.")
                    else:
                        print("Incorrect!.Key is Smaller than you guessed.")
                chances -= 1
        
        if chances == 0:
            print("\nSorry!.You lose the Game.")
            print(f"The correct key is {key}.")
        
        check = continue_or_not()
        
        if check:
            continue
        else:
            print("\nYou terminated the Game...")
            print(f"Games played: {games_played}")
            print(f"Games won: {games_won}")
            print(f"Win Percentage: {round(games_won/games_played,2)*100}%")
            print("Bye!")
            break

if __name__ == "__main__":
    play()