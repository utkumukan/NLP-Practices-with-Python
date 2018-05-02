classifier = nltk.NaiveBayesClassifiers.train(train_set)

#Predict
print(classifier.classify(gender_features('Frank')))