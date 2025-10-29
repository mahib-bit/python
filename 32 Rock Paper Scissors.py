import random

options = ("rock", "papers", "scissors")
running = True
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock , papers, scissors) :").lower()

    print(f"Computer : {computer}")
    print(f"Player : {player}")

    if player == computer:
        print("Draw!!")
    elif computer == "rock" and player == "papers":
        print("You win!!")
    elif computer == "scissors" and player == "rock":
        print("You win!!")
    elif computer == "papers" and player == "scissors":
        print("You win!!")
    else:
        print("You lose!!")
            
    play_again = input("Play again? (Y/N) : ").lower()
    if not play_again == "y":
        running = False

print("Thanks for Playing!")