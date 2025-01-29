from nltk import word_tokenize
from src.preprocess import preprocess
from src.train import extract_training_data, extract_all_words, extract_feature_set, train, extract_features
import random


def chatbot_response(sentence, classifier, response_data, all_words):
    features = extract_features(preprocess(sentence), all_words)
    intent = classifier.classify(features)

    return random.choice(response_data[intent])

def initialize_chatbot(intents, stopwords):
    training_data, response_data = extract_training_data(intents)
    all_words = extract_all_words(training_data, stopwords)
    feature_set = extract_feature_set(training_data, all_words)
    accuracy, classifier = train(feature_set)

    return training_data, response_data, all_words, feature_set, accuracy, classifier

