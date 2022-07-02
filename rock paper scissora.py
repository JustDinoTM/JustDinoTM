import random
from shutil import unregister_archive_format

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_imput = input("type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_imput == "q":
        break

    if user_imput not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper, 1 scissors, 2
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_imput == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_imput == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_imput == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")       
print("Goodbye!")