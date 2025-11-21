# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #7-2 NLTK - Tokenization
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------

# Library
from nltk.tokenize import word_tokenize, sent_tokenize

# Read the text from the file
with open('text.txt', 'r') as textfile:
    text = textfile.read().replace('\n', '')

# Sentence Tokenization
sentence = sent_tokenize(text)

# Word Tokenization
word = word_tokenize(text)

# Output Tokenization
print("< Sentence Tokenization >", "\n", sentence)
print("\n")
print("< Word Tokenization >", "\n", word)

