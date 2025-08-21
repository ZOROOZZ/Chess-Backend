from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Chess API is running!"}

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    move = data.get("move")
    return {"status": "ok", "your_move": move}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
