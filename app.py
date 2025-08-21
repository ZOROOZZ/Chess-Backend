from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend (different domain) to call backend

@app.route("/")
def home():
    return "Chess Backend is running!"

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    row = data.get("row")
    col = data.get("col")

    if row is None or col is None:
        return jsonify({"error": "Missing row or col"}), 400

    # For now, just return a dummy response
    return jsonify({
        "message": f"Move received at row {row}, col {col}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
