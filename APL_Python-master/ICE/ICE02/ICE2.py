'''
  * Python Programming for Data Scientists and Engineers
  * ICE #2
  * Q1 : Frequencies of characters in the string.
  * Q2 : Max word length in the string.
  * Q3 : Count numbers of digits and characters in the string.
  * #11 Chia-Hui Amy Lin
'''

# Prompt user for a sentence
user_input_sentence = input("Please type a sentence you have in mind : ")

# ===================================================================================
# Q1 : Calculate character frequency in a string
characters = list(user_input_sentence)
characters = list(map(lambda x: x.strip(',.'), characters))
characters = " ".join(characters).split()

frequency = {}
for idx in range(len(characters)):
    try:
        frequency[characters[idx]] += 1
    except KeyError:
        frequency[characters[idx]] = 1

# Header
print("\n" + "[ Frequency Count ]")
print("------------------------------------------------------")

# Output frequency count for each character in the user input
for key, val in frequency.items():
    print("Word " + key + " : " + str(val) + " times")

# ===================================================================================
# Q2 : Take a list of words and return the length of the longest one
wordList = user_input_sentence.split()
wordLenCount = {}

for word in range(len(wordList)):
    wordLenCount[wordList[word]] = len(wordList[word])
sort = dict(sorted(wordLenCount.items(), key=lambda x: (-x[1], x[0])))

# Header
print("\n" + "[ Max Word Length ]")
print("------------------------------------------------------")

# Output the max lenght
print("Max word length of this sentence :", list(sort.values())[0])
maxWords = []
for w_key, w_val in sort.items():
    if w_val == list(sort.values())[0]:
        maxWords.append(w_key)

# Output word(s) with the max length
print("Word(s) with max length :")
for selection in range(len(maxWords)):
    print("\t" + maxWords[selection])

# ===================================================================================
# Q3 : Obtain a string and calculate the number of digits and letters

# Header
print("\n" + "[ # of Digits & Letters ]")
print("------------------------------------------------------")

# Filter out the digits in the string
numberList = list(filter(str.isdigit, user_input_sentence))
letterCount = ''.join([letter for letter in user_input_sentence if not letter.isdigit()])

# Output the count for digits and letters in the string
print("Total # of numbers(digits):", len(numberList))
print("Total # of letters:", len(letterCount))

