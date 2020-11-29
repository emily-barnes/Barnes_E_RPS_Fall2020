# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose


# this is the player choice
# player = input("Choose rock, paper, or scissors: ")

# True and False are Boolean data types -> they are the equivalent of on or off, 1 or 0

# set up our game loop
while gameVars.player is False:
    #this is the player choice
    print("================*/ RPS GAME*/====================")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("==========================================")
    print("Choose your weapon! Or type quit to exit\n") #n means "new line"
    gameVars.player = input("Choose rock, paper or scissors: \n")

    # if the gameVars.player
    # chose to quit, then exit the game
    if gameVars.player == "quit":
        print("You chose to quit")
        exit()

    #player = True -> it has a value (rock, paper, or scissors)

    # this will be the AI choice -> a random pick from the choices array
    computer = gameVars.choices[randint(0, 2)]

    # check to see what the user input

    # print outputs whatever is in the round brackets => in this case it outputs player to the command prompt window
    print("user chose: " + gameVars.player)

    # validate that the random choice worked for the AI
    print("AI chose: " + computer)

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

        
    print("Player has", gameVars.player_lives, "lives left")
    print("Computer has", gameVars.computer_lives, "lives left")

    if gameVars.computer_lives == 0:
        winLose.winorlose("won")

        
    print("Player has", gameVars.player_lives, "lives left")
    print("Computer has", gameVars.computer_lives, "lives left")

    # make the loop keep running by setting player back to False
    # unset, so that our loop condition above will evaluate to True
    gameVars.player = False
