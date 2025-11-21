# ------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * LAB #7 Analyze file using NLTK
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------

# Library
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist


# Read the text from the file
with open('theManTrap.txt', 'r') as textfile:
    text = textfile.read().replace('\n', '')

# Word Tokenization + Remove punctuations
word_list = word_tokenize(text)
word_list = [word.lower() for word in word_list if word.isalpha()]

# Remove stopwords from word list
clean_word_list = word_list[:]
for word in word_list:
    if word in stopwords.words('english'):
        clean_word_list.remove(word)

# Count frequency of words + Get top 5 words
word_frequency = FreqDist(clean_word_list)
top5 = {}
for word, frequency in word_frequency.most_common(5):
    #print(u'{}:{} times'.format(word, frequency))
    top5[word] = frequency

# Output results for visualization
outfile = open('summary.txt', 'w')
for key, value in sorted(word_frequency.items()):
    outfile.write(str(key) + '\t' + str(value) + '\n')

# Sentence Tokenization
sentence_list = sent_tokenize(text)
sentToken = FreqDist(sentence_list)

# Pick out the sentences that have the top 5 words
top5_sentence = []
for key, val in top5.items():
    temp = []
    for num in range(len(sentence_list)):
        if key in sentence_list[num]:
            temp.append(sentence_list[num])
    top5_sentence.append(temp)

# Concatenate all the sentences with the same word
new_sentence = []
for num in range(len(top5_sentence)):
    temp_conc = " ".join(top5_sentence[num])
    new_sentence.append([temp_conc])

# Output sentences contains certain keyword
temp_key = list(top5.keys())
sentence_file = open('sentences.txt', 'w')
for num in range(len(top5)):
    sentence_file.write(">>> Word : " + str(temp_key[num]) + "\n" + str(new_sentence[num]))
    sentence_file.write("\n" + "\n")
