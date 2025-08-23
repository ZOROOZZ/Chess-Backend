from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Initial chessboard
board = [
    ["♜","♞","♝","♛","♚","♝","♞","♜"],
    ["♟","♟","♟","♟","♟","♟","♟","♟"],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["♙","♙","♙","♙","♙","♙","♙","♙"],
    ["♖","♘","♗","♕","♔","♗","♘","♖"]
]

@app.route("/")
def home():
    return "Chess Backend is running!"

@app.route("/move", methods=["POST"])
def move():
    global board
    data = request.get_json()
    fr, to = data["from"], data["to"]
    fr_r, fr_c = fr["row"], fr["col"]
    to_r, to_c = to["row"], to["col"]

    piece = board[fr_r][fr_c]
    if piece == "":
        return jsonify({"valid": False, "board": board})

    # ❗ Simple move (no chess rules yet)
    board[to_r][to_c] = piece
    board[fr_r][fr_c] = ""
    return jsonify({"valid": True, "board": board})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
