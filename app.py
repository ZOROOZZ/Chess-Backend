from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)

# Set up CORS: limit to known frontend for production use!
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return jsonify({"message": "Chess Backend is running!"})

def is_valid_move(row, col):
    # Dummy chess move validation, extend this with your actual logic!
    return isinstance(row, int) and isinstance(col, int) and 0 <= row < 8 and 0 <= col < 8

@app.route("/move", methods=["POST"])
def move():
    try:
        data = request.get_json(force=True)
        row = data.get("row")
        col = data.get("col")

        if row is None or col is None:
            logging.warning("Missing row or col in move request")
            return jsonify({"error": "Missing row or col"}), 400

        if not is_valid_move(row, col):
            logging.warning(f"Invalid move: row={row}, col={col}")
            return jsonify({"error": "Invalid move"}), 400

        # Placeholder: extend with your chess game logic.
        logging.info(f"Move received at row {row}, col {col}")
        return jsonify({
            "message": f"Move received at row {row}, col {col}",
            "status": "success"
        })

    except Exception as e:
        logging.error(f"Exception in /move endpoint: {e}")
        return jsonify({"error": "Server error", "details": str(e)}), 500

if __name__ == "__main__":
    # Use host and port from environment variables if available
    import os
    host = os.environ.get("FLASK_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_PORT", 5000))
    app.run(host=host, port=port, debug=True)
