print(" welcome to rock paper scissors!")
print("-" * 40)
import random

game = ["rock", "paper", "scissors"]
computer = random.choice(game)
player = input(" make your move: rock paper or scissors: ").lower()
if computer == "rock":
    if player == computer:
        print(f" it's a draw. the computer chose {computer}")
    elif player == "paper":
        print(f" you won. the computer chose {computer}")
    elif player == "scissors":
        print(f" you lose. the computer chose {computer}")
    else:
        print(" Error!!!!_item n0t foundD :(")

elif computer == "paper":
    if player == computer:
        print(f" it's a draw. the computer chose {computer}")
    elif player == "scissors":
        print(f" you won. the computer chose {computer}")
    elif player == "rock":
        print(f" you lost. the computer chose {computer}")
    else:
        print(" Error!!!!_item n0t foundD :(")

elif computer == "scissors":
    if player == computer:
        print(f" it's a draw. the computer chose {computer}")
    elif player == "rock":
        print(f" you won. the computer chose {computer}")
    elif player == "paper":
        print(f" you lost. the computer chose {computer}")
    else:
        print(" Error!!!!_item n0t foundD :(")
print("-" * 40)
