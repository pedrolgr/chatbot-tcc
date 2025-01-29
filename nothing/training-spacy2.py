import random
import nltk
from data.intent_config import intents
from src.preprocess import lemmatize, tokenize, text_cleaner

training_data = []
response_data = {}

for intent in intents['intents']:
    for pattern in intent['patterns']:
        cleaned_pattern = text_cleaner(pattern)
        lemmatized_pattern = lemmatize(cleaned_pattern)
        training_data.append((lemmatized_pattern, intent['intention']))

    response_data[intent['intention']] = intent['responses']

random.seed(32)
random.shuffle(training_data)



'''
all_words = []
for (pattern, response) in training_data:
    tokens = tokenizer(pattern)

print(all_words)

feature_set = []
for (pattern, intention) in training_data:
    tokens = tokenizer(pattern)
    feature = {word: (word in tokens) for word in all_words}
    feature_set.append((feature, intention))

train_data = feature_set[:int(0.8 * len(feature_set))]
test_data = feature_set[int(0.8 * len(feature_set)):]

print(feature_set)

classifier = nltk.NaiveBayesClassifier.train(train_data)

accuracy = nltk.classify.accuracy(classifier, test_data)

print(accuracy)

def extract_features(sentence):
    tokens = word_tokenize(sentence.lower())
    return {word: (word in tokens) for word in all_words}


def chatbot_response(sentence):
    # Classificar a intenção
    features = extract_features(sentence)
    intent = classifier.classify(features)

    # Retornar uma resposta aleatória para a intenção classificada
    return random.choice(response_data[intent])


# Testar o chatbot
while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Chatbot: Até mais! 😊")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
'''