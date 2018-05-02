from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = list(stopwords.words('turkish'))
words = word_tokenize(data)
stopWordsFiltered = []

for i in words:
    if i in stopWords:
        stopWordsFiltered.append(i)

print(stopWordsFiltered)
print(stopWords)