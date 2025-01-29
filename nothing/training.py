import random
import nltk
from nltk import word_tokenize, WordNetLemmatizer
import re
from data.intent_config import intents

lemmatizer = WordNetLemmatizer()

with open('../data/stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set(line.strip() for line in file)

training_data = []
response_data = {}

for intent in intents['intents']:
    for pattern in intent['patterns']:
        pattern = pattern.lower()
        pattern = re.sub(r'[^\w\s]', '', pattern)
        words = pattern.split()
        lemmatized_pattern = " ".join([lemmatizer.lemmatize(word) for word in words])
        print(lemmatized_pattern)
        training_data.append((lemmatized_pattern, intent['intention']))

    response_data[intent['intention']] = intent['responses']

print(training_data)

random.seed(32)
random.shuffle(training_data)

all_words = []
for (pattern, response) in training_data:
    tokens = word_tokenize(pattern.lower())
    [all_words.append(token) for token in tokens if token not in all_words and token not in stopwords]


feature_set = []
for (pattern, intention) in training_data:
    tokens = word_tokenize(pattern.lower())
    feature = {word: (word in tokens) for word in all_words}
    feature_set.append((feature, intention))

train_data = feature_set[:int(0.8 * len(feature_set))]
test_data = feature_set[int(0.8 * len(feature_set)):]

print(train_data)
print(test_data)

classifier = nltk.NaiveBayesClassifier.train(train_data)

accuracy = nltk.classify.accuracy(classifier, test_data)
print(accuracy)

def extract_features(sentence):
    tokens = word_tokenize(sentence.lower())
    return {word: (word in tokens) for word in all_words}


def chatbot_response(sentence):
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
