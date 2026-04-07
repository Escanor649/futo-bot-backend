from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 
import nltk
from nltk.tokenize import word_tokenize
import json
import random

nltk.download('punkt_tab') 

app = Flask(__name__)
# ... the rest of your code stays exactly the same
nltk.download('punkt_tab') 

app = Flask(__name__)
CORS(app)

with open('intents.json', 'r') as file:
    intents = json.load(file)

def get_bot_response(user_input):
    user_words = set(word_tokenize(user_input.lower()))
    
    best_intent = None
    max_matches = 0
    
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_words = set(word_tokenize(pattern.lower()))
            matches = len(user_words.intersection(pattern_words))
            
            if matches > max_matches:
                max_matches = matches
                best_intent = intent

    if max_matches > 0:
        return random.choice(best_intent['responses'])
    else:

        return "sorry, i'm unable to answer that" [cite: 1]
@app.route("/")
def home():
    return "FUTO Bot Backend is Active!"

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = get_bot_response(msg)
    return response

if __name__ == "__main__":
    app.run(debug=True)
