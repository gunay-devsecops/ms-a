from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        service="service-a",
        status="running"
    )

@app.route("/call-b")
def call_b():
    return jsonify(
        message="service-a will call service-b later"
    )

app.run(host="0.0.0.0", port=5000)
