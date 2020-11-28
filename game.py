# import packages to extend python (just like we extend sublime, or Atom, or VSCode)
from random import randint


# create a variable stack - bits of data that can (and will) change

# [] => this is an array. an array is a special type of container that can hold multiple items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]



player_lives = 5
computer_lives = 5

total_lives = 5

# define a win or lose function
def winorlose(status):
    #print("inside winorlose function; status is:", status)

    print("You", status, "! Would you like to play again?")
    choice = input("Y / N")
    
    if choice == "N" or choice == "n":
        print("You chose to quit! Better luck next time!")
        exit()

    elif choice == "Y" or choice == "y":
        # reset the player lives and the computer lives
        # and set the player to False so that our loop will restart
        global player_lives
        global computer_lives
        global player

        player_lives = 5
        computer_lives = 5
        player = False

    else:
        print("Make a valid choice - Y or N")
        # this will generate a bug that we need to fix later
        choice = input("Y / N")

# this is the player choice
# player = input("Choose rock, paper, or scissors: ")

# True and False are Boolean data types -> they are the equivalent of on or off, 1 or 0
player = False

while player is False:
    print("================*/ RPS GAME*/====================")
    print("Computer Lives:", computer_lives, "/", total_lives)
    print("Player Lives:", player_lives, "/", total_lives)
    print("==========================================")

    print("Choose your weapon! Or type quit to exit\n") #n means "new line"
    # this is the player choice
    player = input("Choose rock, paper or scissors: \n")

    # if the player chose to quit, then exit the game
    if player == "quit":
        print("You chose to quit")
        exit()

    #player = True -> it has a value (rock, paper, or scissors)

    # this will be the AI choice -> a random pick from the choices array
    computer = choices[randint(0, 2)]

    # check to see what the user input

    # print outputs whatever is in the round brackets => in this case it outputs player to the command prompt window
    print("user chose: " + player)

    # validate that the random choice worked for the AI
    print("AI chose: " + computer)

    if (computer == player):
        print("tie")

    # always check for negative conditions first (the losing case)
    elif (computer == "rock"):
        if (player == "scissors"):
            print("You lose!")
            player_lives -= 1
        else:
            print("You win!")
            computer_lives -= 1

    elif (computer == "paper"):
        if (player == "scissors"):
            print("You lose!")
            player_lives -= 1
        else:
            print("You win!")
            computer_lives -= 1

    elif (computer == "scissors"):
        if (player == "paper"):
            print("You lose!")
            player_lives -= 1
        else:
            print("You win!")
            computer_lives -= 1

    if player_lives is 0:
        winorlose("lost")

        

    print("Player has", player_lives, "lives left")
    print("Computer has", computer_lives, "lives left")

    if computer_lives is 0:
        winorlose("won")

        

    print("Player has", player_lives, "lives left")
    print("Computer has", computer_lives, "lives left")

    # make the loop keep running by setting player back to False
    # unset, so that our loop condition above will evaluate to True
    player = False
