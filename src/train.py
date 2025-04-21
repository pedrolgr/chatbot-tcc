import random
from nltk import word_tokenize
import nltk
from src.preprocess import preprocess

def extract_training_data(intents):
    training_data = []
    response_data = {}
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            training_data.append((preprocess(pattern), intent['intention']))
        response_data[intent['intention']] = intent['responses']
    random.shuffle(training_data)
    print(training_data)

    return training_data, response_data

def extract_all_words(training_data, stopwords):
    all_words = []
    for (pattern, intention) in training_data:
        tokens = word_tokenize(pattern)
        [all_words.append(token) for token in tokens if token not in all_words and token not in stopwords]

    return all_words

def extract_feature_set(training_data, all_words):
    feature_set = []
    for (pattern, intention) in training_data:
        tokens = word_tokenize(pattern)
        feature = {word: (word in tokens) for word in all_words}
        feature_set.append((feature, intention))

    return feature_set

def extract_features(sentence, all_words):
    tokens = word_tokenize(sentence.lower())
    return {word: (word in tokens) for word in all_words}

def train(feature_set):
    train_data = feature_set[:int(0.8 * len(feature_set))]
    test_data = feature_set[int(0.8 * len(feature_set)):]
    classifier = nltk.NaiveBayesClassifier.train(train_data)
    accuracy = nltk.classify.accuracy(classifier, test_data)

    return accuracy, classifier

