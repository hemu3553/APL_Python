# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #7-4 NLTK - POS
#  * #11 Chia-Hui Amy Lin
# --------------------------------------------------------------------

# Library
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Read the text from the file
with open('text.txt', 'r') as textfile:
    text = textfile.read().replace('\n', '')

# Take out the non-word in the list and breakdown into words
word_list = (text.replace(".", " ")).split()

# Remove duplicates
word_list = list(set(word_list))

# Get the token for the texts and put tags on each of them
textToken = word_tokenize(text)
tagToken = pos_tag(textToken)

# Output Text Tokens
print("< Text Tokens: >")
for token in range(len(textToken)):
    print(textToken[token])

# Output Tag Tokens
print("< Tag Tokens: >")
for token in range(len(tagToken)):
    print(tagToken[token])
