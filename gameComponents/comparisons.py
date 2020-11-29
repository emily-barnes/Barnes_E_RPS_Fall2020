if (computer == gameVars.player):
        print("tie")

    # always check for negative conditions first (the losing case)
    elif (computer == "rock"):
        if (gameVars.player == "scissors"):
            print("You lose!")
            gameVars.player_lives -= 1
        else:
            print("You win!")
            gameVars.computer_lives -= 1

    elif (computer == "paper"):
        if (gameVars.player == "scissors"):
            print("You lose!")
            gameVars.player_lives -= 1
        else:
            print("You win!")
            gameVars.computer_lives -= 1

    elif (computer == "scissors"):
        if (gameVars.player == "paper"):
            print("You lose!")
            gameVars.player_lives -= 1
        else:
            print("You win!")
            gameVars.computer_lives -= 1

    if gameVars.player_lives == 0:
        winLose.winorlose("lost")
