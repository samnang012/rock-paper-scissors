import random

choices = ['rock', 'paper', 'scissors']
computerScore = 0
userScore = 0
WinScore = 2

while userScore < WinScore and computerScore < WinScore:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice not in choices:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print("User: ", user_choice)
    print("Computer: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        userScore += 1
        print("You win this round!")
    else:
        computerScore += 1
        print("Computer wins this round!")

if (userScore == WinScore):
    print("You win the game!")
elif (computerScore == WinScore):
    print("Computer wins the game!")
