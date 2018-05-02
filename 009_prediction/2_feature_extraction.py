featuresets = [(gender_features(n), g) for (n,g) in names]

def gender_features(word):
    return {'last_letter': word[-1]}