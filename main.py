from src.chatbot import initialize_chatbot, chatbot_response

from data.intent_config import intents

with open('./data/stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set(line.strip() for line in file)

response_data, all_words, accuracy, classifier = initialize_chatbot(intents, stopwords)

print(accuracy)

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Chatbot: Até mais! 😊")
        break
    response = chatbot_response(user_input, classifier, response_data, all_words)
    print(f"Chatbot: {response}")