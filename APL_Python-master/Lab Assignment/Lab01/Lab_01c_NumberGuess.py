'''
  * Python Programming for Data Scientists and Engineers
  * LAB #1-c Guess the number that is randomly picked by the program.
  * #11 Chia-Hui Amy Lin
'''

# Import random library using randint
from random import randint

# Set variables : count and a random number
count = 4
randomNum = randint(0, 9)

# Welcome header
print("Welcome to the number guessing game! :D" + "\n" + "You have 5 chances to guess..")
print("----------------------------------------------------------------------")

# Main body of the game
flag = False

# If the player guess wrong and still have chances left, continue the game
while count >= 0:
    while True:
        # Prompt user for a number guess between 0 and 9
        player_guess = input("Please guess a number between 0 and 9 : ")

        # Error check for invalid input
        try:
            iplayer_guess = int(player_guess)
        except ValueError or TypeError:
            print("Invalid input. Please enter an INTEGER." + "\n")
            flag = True
        else:
            break
    # Right answer: exit the game and congrats the player!
    if int(player_guess) == randomNum:
        print("+++ Congratulation! You hit a jack-pot! That's the right number! +++")
        exit()
    else:
        # Wrong answer : Prompt player for another try until the chances ran out
        if count != 0:
            print("You guess the wrong number. Take another guess!")
            # Hints of whether the number is smaller or bigger
            if int(player_guess) > randomNum:
                print("| HINT : Guess a bigger number. |" + "\n")
            else:
                print("| HINT : Guess a smaller number. |" + "\n")
            print("[Chances Left -> ", count, "]")  # Display the number of attempts left
        else:
            # End of the game statement
            print("\n" + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx END OF GAME xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx " \
                  + "\n" + "You ran out of chances to guess!")
            print("Have a better luck at guessing next time!")

        flag = True
        count -= 1  # Decrement player's chances to try



