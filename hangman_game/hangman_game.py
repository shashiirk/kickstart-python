from random import choice
from words import word_list

def get_letter():

    c = input("Guess a letter: ")
    
    if c.isalpha():
        return c.upper()
    else:
        print("Plese enter an alphabet!")
        return get_letter()

def continue_or_not():
    
    c = input("Do you want to continue (Y|N)? ")
    
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
    print(f"\n{7*'='} HANGMAN GAME {7*'='}")
    print("Find the correct word to win the game.")

    while True:
        games_played += 1
        key = choice(word_list).upper()
        chances = 6
        guesses = []
        word = " ".join(list('_'*len(key)))
        
        while chances != 0:
            print(f"\nPrevious Guesses: {' '.join(guesses)}")
            print(f"Chances left: {chances}")
            print(f"Word: {word}")
            
            c = get_letter()
            
            if c in key:
                if c in word:
                    print("You already guessed this letter.")
                else:
                    print(f"Whew! {c} is in the word.")
                    x = [i for i,value in enumerate(key) if value==c]
                    word = word.split()
                    for i in x:
                        word[i] = c
                    word = ' '.join(list(word))
                    
                    if str(''.join(word.split())) == key:
                        games_won += 1
                        print(f"\nCongrats!.You guessed {key} correctly.")
                        print("You won the game.\n")
                        break
            else:
                if c in guesses:
                    print("You already guessed this letter.")
                else:
                    print(f"Oops! {c} is not in the word.")
                    guesses.append(c)
                    chances -= 1
        
        if chances == 0:
            print(f"\nSorry!.You lose the game.")
            print(f"The correct word is {key}\n")
        
        check = continue_or_not()

        if check:
            continue
        else:
            print("\nYou terminated the game...")
            print(f"Games Played: {games_played}")
            print(f"Games Won: {games_won}")
            print(f"Win Percentage: {round(games_won/games_played,2)*100}%")
            print("Bye!")
            break

if __name__ == "__main__":
    play()