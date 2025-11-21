# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #7-7 NLTK - Named Entity Recognition
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------

# Library
from nltk import pos_tag, ne_chunk
from nltk.tokenize import wordpunct_tokenize

# Read the text from the file
with open('text.txt', 'r') as textfile:
    text = textfile.read().replace('\n', '')

# Take out the non-word in the list and breakdown into words
word_list = (text.replace(".", " ")).split()

# Remove duplicates
word_list = list(set(word_list))

# Get the token for the texts and put tags on each of them
namedEntity = ne_chunk(pos_tag(wordpunct_tokenize(text)))

# Output Named Entity Recognition
print("< Named Entity Recognition : >")
print(namedEntity)
