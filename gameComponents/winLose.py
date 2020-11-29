from gameComponents import gameVars

#define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    #print("inside winorlose function; status is:", status)

    if status == "won":
        pre_message = "You are the winner!"
    else:
        pre_message = "You lost!!"

    print(pre_message + "Would you like to play again?")

    choice = input("Y / N")
    

    if choice == "Y" or choice == "y":
        # reset the player lives and the computer lives
        # and set the player to False so that our loop will restart
        gameVars.player_lives
        gameVars.computer_lives
        gameVars.player = False

    
    elif choice == "N" or choice == "n":
        print("You chose to quit! Better luck next time!")
        exit()

    else:
        print("Make a valid choice - Y or N")
        # this will generate a bug that we need to fix later
        choice = input("Y / N")
