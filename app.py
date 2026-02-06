from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

jokes = [
    {"id": 1, "setup": "Why did the programmer quit his job?", "punchline": "Because he didn't get arrays."},
    {"id": 2, "setup": "How do you comfort a JavaScript bug?", "punchline": "You console it."},
    {"id": 3, "setup": "What is a keyboard's favorite food?", "punchline": "Space bars."}
]


@app.route('/')
def home():
    return "Welcome to the Joke API! Use /jokes/random to get a random joke."


@app.route('/jokes/random', methods=['GET'])
def get_a_joke():
    joke = random.choice(jokes)
    return jsonify(joke)


@app.route('/aqibjaved')
def aqibinfo():
    return "This Api is powered by Aqibjaved it is currently a WIP!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
