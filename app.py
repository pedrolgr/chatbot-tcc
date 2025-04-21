from flask import Flask, render_template, request, jsonify
from src.chatbot import initialize_chatbot, chatbot_response
from data.intent_config import intents

app = Flask(__name__, template_folder="pages/templates", static_folder="pages/static")

with open('./data/stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set(line.strip() for line in file)

response_data, all_words, accuracy, classifier = initialize_chatbot(intents, stopwords)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/response", methods=["GET"])
def responder():
    message = request.args.get("message")
    response = chatbot_response(message, classifier, response_data, all_words)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()
