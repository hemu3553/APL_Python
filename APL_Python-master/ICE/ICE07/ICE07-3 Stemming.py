# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #7-3 NLTK - Stemming
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------

# Library
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

# Initialize lists
stemmerList = []
lancasterList = []
snowballList = []

# Read the text from the file
with open('text.txt', 'r') as textfile:
    text = textfile.read().replace('\n', '')

# Take out the non-word in the list and breakdown into words
word_list = (text.replace(".", " ")).split()

# Remove duplicates
word_list = list(set(word_list))

# Output words with 3 different stemming algorithms
# Porter Stemming Algorithm
print("<< Porter Stemming Algorithm >>")
for idx in range(len(word_list)):
    porterstemmer = PorterStemmer()
    stemmerList.append(porterstemmer.stem(word_list[idx]))
    print(">>> Word : ", stemmerList[idx])
print("\n")

# Lancaster Stemmer Algorithm
print("<< Lancaster Stemmer Algorithm >>")
for idx in range(len(word_list)):
    lancasterstemmer = LancasterStemmer()
    lancasterList.append(lancasterstemmer.stem(word_list[idx]))
    print(">>> Word : ", lancasterList[idx])
print("\n")

# Snowball Stemmer Algorithm
print("<< Snowball Stemmer Algorithm >>")
for idx in range(len(word_list)):
    snowballstemmer = SnowballStemmer('english')
    snowballList.append(snowballstemmer.stem(word_list[idx]))
    print(">>> Word : ", snowballList[idx])
