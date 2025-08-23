from flask import Flask, request, jsonify
from flask_cors import CORS

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

    # ❗ Here you would add proper chess logic
    board[to_r][to_c] = piece
    board[fr_r][fr_c] = ""
    return jsonify({"valid": True, "board": board})

if __name__ == "__main__":
    app.run(debug=True)
