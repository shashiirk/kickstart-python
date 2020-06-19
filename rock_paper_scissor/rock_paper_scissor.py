import random

def get_user_choice():

    user_choice = input("Enter your choice: ").upper()
    
    if user_choice not in ['R','P','S']:
        return get_user_choice()
    else:
        return user_choice

def find_winner(user_choice,computer_choice):
    
    if(user_choice == computer_choice):
        return None
    elif(user_choice == 'R'):
        if(computer_choice == 'P'):
            return "Computer"
        else:
            return "You"
    elif(user_choice == 'P'):
        if(computer_choice == 'R'):
            return "You"
        else:
            return "Computer"
    else:
        if(computer_choice == 'R'):
            return "Computer"
        else:
            return "You"

def play():
    
    print(f"{7*'='} ROCK PAPER SCISSOR GAME {7*'='}\n")
    print("Keyboard Controls:")
    print("R: Rock \nP: Paper \nS: Scissor \n")

    symbols = {'R':"Rock", 'P':"Paper", 'S':"Scissor"}

    games_played = 0
    games_won = 0

    while True:
        games_played += 1
        user_choice = get_user_choice()
        computer_choice = random.choice(list(symbols.keys()))

        winner = find_winner(user_choice,computer_choice)
        
        if winner is not None:
            if winner == "You":
                games_won += 1
                print(f"Your choice: {symbols[user_choice]}")
                print(f"Computer choice: {symbols[computer_choice]}")
                print("Hurray! You won the game!!!")
            else:
                print(f"Your choice: {symbols[user_choice]}")
                print(f"Computer choice: {symbols[computer_choice]}")
                print("Oops! Computer won the game!!!")
        else:
            print(f"Your choice: {symbols[user_choice]}")
            print(f"Computer choice: {symbols[computer_choice]}")
            print("Hmmm! The Game is drawn!!!")
        if input("\nPlay again...? (Y/N) : ").upper() != 'Y':
            break

    print("\nYou terminated the Game...")
    print(f"Games played: {games_played}")
    print(f"Games won: {games_won}")
    print(f"Win Percentage: {round(games_won/games_played,2)*100}%")
    print("Bye!")

if __name__ == "__main__":
    play()