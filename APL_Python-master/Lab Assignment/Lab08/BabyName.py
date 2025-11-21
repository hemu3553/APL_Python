# ------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #8 Baby Name Generator using Markov Chains
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------

# Library
import nltk
import random
from collections import Counter
import json

# A name generator function
def nameGenerator(nameList, length):
    CharList = []
    keyList = []
    valList = []

    # Count the occurrences of each character in the file and put into the dictionary {character : count}
    for idx in range(len(nameList)):
        CharList += list(nameList[idx].lower())
    charCount = dict(Counter(CharList))

    # Separate Character and Count into different dictionaries
    for key, val in charCount.items():
        keyList.append(key)
        valList.append(val)

    # Call nltk package for real words list
    english_vocab = set(realword.lower() for realword in nltk.corpus.words.words())

    # Generate a series of random characters based on the weighted counts and user's choice of word length
    # The more often a character appears, the higher chance it will be selected
    randomlist = random.choices(keyList, valList, k=length)

    # Put the characters into a word and check if it exists or not
    # If not, generate a new set of characters until it's a real word
    while "".join(randomlist) not in english_vocab:
        randomlist = random.choices(keyList, valList, k=length)
    newName = randomlist[0].upper() + "".join(randomlist[1::])

    return newName

def main():
    girlname = []
    boyname = []

    # Read in the National Name file and split the female and male names into different lists
    with open('2016NationalName.txt') as file:
        text = file.readlines()
        text = [index.strip() for index in text]
        for num in range(len(text)):
            if "F" in text[num]:
                girlname.append(text[num].split(',')[0])
            else:
                boyname.append(text[num].split(',')[0])

    # Gender prompt from the user
    flag = False
    while True:
        genderPrompt = input("Would you like a boy or girl name? ( B/b for boy ; G/g for girl ) : ")
        if genderPrompt.lower() == "b" or genderPrompt.lower() == "g":
            flag = False

            # Name Length prompt from the user
            while True:
                namelenPrompt = input("How many characters for the name? ")

                # Error handling if length is not numeric or less than 1 character
                try:
                    namelenPrompt = int(namelenPrompt)
                except ValueError or TypeError or namelenPrompt < 1:
                    print("Invalid input. Please enter an INTEGER." + "\n")
                    error = True
                else:
                    break

            # Generate the baby's name for a Girl
            if genderPrompt.lower() is "g":
                babyName = nameGenerator(girlname, namelenPrompt)

            # Generate the baby's name for a Boy
            else:
                babyName = nameGenerator(boyname, namelenPrompt)
            break

    print("Your baby's name will be : ", babyName)


if __name__ == "__main__":
    main()


# Put the data into JSON form
'''
JSONList = []

with open('2016NationalName.txt') as file, open("formatOutput.json", "w") as outputFile:
    Info = file.readlines()
    Info = [index.strip() for index in Info]
    for num in range(len(Info)):
        girlJSON = \
            {
                "Name": Info[num].split(',')[0],
                "Gender": Info[num].split(',')[1],
                "Count": Info[num].split(',')[2],
            }
        JSONList.append(girlJSON)
    outputFile.write(json.dumps(JSONList))
'''
