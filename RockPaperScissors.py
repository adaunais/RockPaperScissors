import random 

while True:

    playerScore = 0
    computerScore = 0
    choice = ''



    while choice != 'quit' and computerScore < 5 and playerScore < 5:
        options = ["rock", "paper", "scissors", "quit"]
        computerOptions = ["rock", "paper" , "scissors"]
 

        print(f"Players Score: {playerScore}\n")
        print(f"Opponents Score: {computerScore}\n")

        print("This is a game of rock paper scissors!\n")
        print("Make your choice player!\n")
        choice = input("ROCK, PAPER, OR SCISSORS!\n")
        choice = choice.lower()
        computerChoice = random.choice(computerOptions)

        if choice not in options:
            print("Invalid choice, try again.")
            continue



        if choice == computerChoice:
            print("ITS A TIE")

        elif choice == "rock" and computerChoice == "scissors" or choice == "paper" and computerChoice == "rock" or choice == "scissors" and computerChoice == "paper":
            print(f"You chose {choice}\n")
            print(f"Oppenent chose {computerChoice}\n")
            print("YOU WIN!\n")
            playerScore = playerScore + 1

        elif choice == "rock" and computerChoice == "paper" or choice == "paper" and computerChoice == "scissors" or choice == "scissors" and computerChoice == "rock":
            print(f"You chose {choice}\n")
            print(f"Oppenent chose {computerChoice}\n")
            print("YOU LOSE!\n")
            computerScore = computerScore + 1
        
        elif choice == 'quit' or playerScore == 5 or computerScore ==5:
            break

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break





