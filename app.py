from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room, leave_room
import chess
import chess.engine
import eventlet
import os

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory games dict: {game_id: chess.Board()}
games = {}

@app.route('/')
def home():
    return jsonify({"message": "Chess backend running"})

@app.route('/create_game', methods=["POST"])
def create_game():
    import uuid
    game_id = str(uuid.uuid4())
    games[game_id] = chess.Board()
    return jsonify({"game_id": game_id})

@app.route('/move', methods=["POST"])
def move():
    data = request.get_json()
    game_id = data.get('game_id')
    uci_move = data.get('move')

    if game_id not in games:
        return jsonify({"error": "Invalid game ID"}), 404

    board = games[game_id]
    try:
        move = chess.Move.from_uci(uci_move)
        if move in board.legal_moves:
            board.push(move)
            # If AI enabled - make AI move (simple in this example)
            # Uncomment and set up AI if desired
            
            # For now just return board fen and status
            return jsonify({
                "status": "ok",
                "fen": board.fen(),
                "legal_moves": [m.uci() for m in board.legal_moves],
                "is_check": board.is_check(),
                "is_checkmate": board.is_checkmate(),
                "is_stalemate": board.is_stalemate(),
                "turn": "white" if board.turn else "black",
                "game_over": board.is_game_over()
            })
        else:
            return jsonify({"error": "Illegal move"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')

