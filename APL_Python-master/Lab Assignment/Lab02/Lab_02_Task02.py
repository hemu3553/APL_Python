'''
  * Python Programming for Data Scientists and Engineers
  * LAB #2-2 Check if the string contains all letters of the alphabet.
  * #11 Chia-Hui Amy Lin
'''
# Library import
import string

# A set for all the alphabets in lowercase
alphabet_set = set(string.ascii_lowercase)

# Prompt for user input ( either a sentence or word )
user_input = input("Please enter a sentence or word to check if all alphabets are included : ")

# Convert the string into lower case, took out non-alphabet symbols
# And put into one string without spaces
user_input = (map(lambda x: x.strip(',.'), user_input.lower()))
user_input = set(" ".join(user_input).split())

# Check if every alphabet is in the user input string
# If True, congrats user!
if user_input == alphabet_set:
    print("\n", "Bingo! You got every single alphabets!")

# If False, let user know and print out a sorted list of missing alphabets
else:
    missingList = list(alphabet_set - user_input)
    missing_alphabets = sorted(missingList, reverse=False)
    print("\n Uh Oh. Seems like you're missing some alphabets.")
    print("--> Missing alphabets :", missing_alphabets)

