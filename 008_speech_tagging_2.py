import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

document = "Today the Netherlands celebrates King\'s Day. To honor this tradition, the Dutch embassy in San Francisco invited me to"
sentences = nltk.sent_tokenize(document)

data = []
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))

for word in data:
    if 'NNP' in word[1]:
        print(word)