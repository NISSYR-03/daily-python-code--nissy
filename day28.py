from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Nissy's API 🚀"

@app.route("/info")
def info():
    data = {
        "name": "Nissy",
        "course": "CSE",
        "goal": "Software Engineer"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
