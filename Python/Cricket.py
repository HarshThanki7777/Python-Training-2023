import random

def toss_coin():
    """Tosses a coin and returns 'heads' or 'tails'."""
    return random.choice(['heads', 'tails'])

def play_super_over():
    """Plays the super over."""
    user_score = 0
    computer_score = 0
    for _ in range(6):
        user_run = random.randint(0, 6)
        computer_run = random.randint(0, 6)
        user_score += user_run
        computer_score += computer_run
    print("Super Over Results:")
    print("User:", user_score, "Computer:", computer_score)
    if user_score > computer_score:
        print("User wins the super over!")
    elif computer_score > user_score:
        print("Computer wins the super over!")
    else:
        print("Super over ends in a tie!")

def play_match():
    """Plays the main cricket match."""
    toss = toss_coin()
    print("Tossing the coin...")
    user_choice = input("Heads or tails? ").lower()
    if user_choice != 'heads' and user_choice != 'tails':
        print("Invalid choice. Exiting the game.")
        return
    
    print("Coin is tossed! It's", toss)
    if toss == user_choice:
        print("You won the toss!")
        print("Choose whether you want to bat or bowl.")
        user_decision = input("Enter 'bat' or 'bowl': ").lower()
        if user_decision == 'bat':
            print("You chose to bat first.")
            user_score = play_innings()
            computer_score = play_innings()
        elif user_decision == 'bowl':
            print("You chose to bowl first.")
            computer_score = play_innings()
            user_score = play_innings()
        else:
            print("Invalid decision. Exiting the game.")
            return
    else:
        print("You lost the toss. Computer will bat first.")
        computer_score = play_innings()
        user_score = play_innings()
    
    print("Match Results:")
    print("User:", user_score, "Computer:", computer_score)
    if user_score > computer_score:
        print("User wins the match!")
    elif computer_score > user_score:
        print("Computer wins the match!")
    else:
        print("Match ends in a tie!")
        play_super_over()

def play_innings():
    """Plays a single innings and returns the total score."""
    total_score = 0
    wickets = 0
    overs = 0
    balls = 0
    while overs < 5 and wickets < 10:
        runs = random.randint(0, 6)
        total_score += runs
        balls += 1
        if balls == 6:
            overs += 1
            balls = 0
            print("End of over", overs, "- Total:", total_score, "Wickets:", wickets)
        if runs == 0:
            wickets += 1
            print("Wicket! Total:", total_score, "Wickets:", wickets)
            if wickets == 10:
                break
    return total_score

# Start the game
print("Welcome to the Cricket Game!")
play_match()
