import nltk
from nltk.tokenize import PunktSentenceTokenizer

document = "Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python."
sentence = nltk.sent_tokenize(document)
for sent in sentence:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))