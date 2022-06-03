import random

game_list = ['Rock', 'Paper', 'Scissors']


# the loop
while True:
    computer_choice = random.choice(game_list)
    print("Rock = R, Paper = P, Scissors = S, Quit = Q ")
    command = input("pick an option 'R', 'P', 'S' or 'Q: ")
    

    if command.lower() == computer_choice:
        print("Tie")
    elif command.lower() == 'rock' or command.lower() == "r":
        if computer_choice == 'Scissors':
            print("Player won!")
            print("Player: (Rock) : CPU: (" + computer_choice +")")
            break
        else:
            print("Computer won!")
            print("Player: (Rock) : CPU: (" + computer_choice +")")
            break
    elif command.lower() == 'Paper' or command.lower == "p":
        if command.lower() == 'rock' or command.lower == "r":
            print("Player won!")
            print("Player: (Paper) : CPU: (" + computer_choice +")")
            break
        else:
            print("Computer won!")
            print("Player: (Paper) : CPU: (" + computer_choice +")")
            break
    elif command.lower() == 'scissors' or command.lower() == "s":
        if computer_choice == 'Paper':
            print("Player won!")
            print("Player: (Scissors) : CPU: (" + computer_choice +")")
            break
        else:
            print("Computer won!")
            print("Player: (Scissors) : CPU: (" + computer_choice +")")
            break
    elif command.lower() == 'quit' or command.lower() == "q":
        print("You Quit")
        break
    else:
        print("Not amongst our options choose a valid option ")

