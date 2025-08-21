from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    move = data.get("move")
    # for now just return dummy response
    return jsonify({"result": f"Move {move} received!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
