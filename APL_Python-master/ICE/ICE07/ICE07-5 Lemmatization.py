# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #7-5 NLTK - Lemmatization
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------

# Library
from nltk.stem import WordNetLemmatizer

# Initialize lists
lemmatizationList = []
POSList = []

# Read the text from the file
with open('text.txt', 'r') as textfile:
    text = textfile.read().replace('\n', '')

# Take out the non-word in the list and breakdown into words
word_list = (text.replace(".", " ")).split()

# Remove duplicates
word_list = list(set(word_list))

# Normalize the text
for idx in range(len(word_list)):
    normalizeText = WordNetLemmatizer()
    lemmatizationList.append(normalizeText.lemmatize(word_list[idx]))
    POSList.append(normalizeText.lemmatize(word_list[idx], pos='v'))

# Output Lemmatization
print("< Lemmatization >")
for word in range(len(word_list)):
    print(">>>Word: ", lemmatizationList[word])

print("\n")

# Output Lemmatization with POS
print("< Lemmatization with POS >")
for word in range(len(word_list)):
    print(">>>Word: ", POSList[word])
