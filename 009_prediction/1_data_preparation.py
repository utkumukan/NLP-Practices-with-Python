from nltk.corpus import names

#Load data and training
names = ([(name, 'male') for name in names.words('male.txt')]+
         [(name, 'female') for name in names.words('female.txt')])

for names in names:
    print(names)
