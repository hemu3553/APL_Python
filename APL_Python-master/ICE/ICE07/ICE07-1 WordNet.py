# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #7-1 NLTK - Wordnet
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------

# Library
from nltk.corpus import wordnet as wn

# Read the text from the file
with open('text.txt', 'r') as textfile:
    text = textfile.read().replace('\n', '')

# Take out the non-word in the list and breakdown into words
word_list = (text.replace(".", "")).split()

# Remove duplicates
word_list = list(set(word_list))

# Output words with information
for idx in range(len(word_list)):
    word_synsets = wn.synsets(word_list[idx])
    print(">>> Word : ", word_list[idx])
    print(word_synsets)

    # Obtain any synonyms and definitions of words
    for synset in word_synsets:
        if len(synset.examples()) > 1:
            print("Synset Name:", synset.name())
            print("POS Tag:", synset.pos())
            print("Definition:", synset.definition())
            print("Example(s):", synset.examples())
