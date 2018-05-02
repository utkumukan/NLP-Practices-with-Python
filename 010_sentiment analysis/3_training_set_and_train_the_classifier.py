#Our training set is then the sum of these three feature sets:7

train_set = negative_features + positive_features + neutral_features

#We train the classifier:

classifier = NaiveBayesClassifier.train(train_set)

#And make predictions.