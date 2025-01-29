import random
from nltk import word_tokenize
import nltk
from data.intent_config import intents
from src.preprocess import preprocess

with open('../data/stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set(line.strip() for line in file)

def extract_features(sentence):
    tokens = word_tokenize(sentence)
    return {word: (word in tokens) for word in all_words}


def chatbot_response(sentence):
    features = extract_features(preprocess(sentence))
    intent = classifier.classify(features)

    return random.choice(response_data[intent])


# Testar o chatbot
while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Chatbot: Até mais! 😊")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
