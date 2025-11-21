# ------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #4-c Sorted Comma Separated Sequence
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------
# An empty list to store words entered by user
wordList = []

# Prompt user how many words he/she wants to enter
error = False
while True:
    try:
        count_num = int(input("How many word(s) do you want to enter? "))
        break

# Error detection if the input is not a number & prompt user again
    except ValueError:
        print("Please enter a valid number.", "\n")
        error = True

# Prompt user for words until it's the same as the number from the previous prompt
while len(wordList) < count_num:
    word = input("Please enter a word : ")
    # If the user entered more than a word, split into individual words
    if " " in word:
        print("\n")
        print("[ Seems like you entered more than a word. Automatically splitting ... ]", "\n")
        wordList += word.split()
    else:
        # If it's a word, append it to the wordList
        wordList.append(word)

# Output original word list and sorted list
print("Entered Words : ", wordList)
wordList.sort()
print("Sorted List : ", wordList)
