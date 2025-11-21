# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #7-6 NLTK - Trigram
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------

# Library
from nltk import trigrams
import nltk

# Read the text from the file
with open('text.txt', 'r') as textfile:
    text = textfile.read().replace('\n', '')

# Obtain tokens
textToken = nltk.word_tokenize(text)
textToken = [token.lower() for token in textToken if len(token) > 1]
trigram_tokens = trigrams(textToken)

# Output counts from trigram
print("< Trigram Output >")
for item in trigram_tokens:
    print(item)
