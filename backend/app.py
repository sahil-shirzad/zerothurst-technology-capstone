from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

incidents = [
    {"id": 1, "title": "Phishing Email", "status": "Open"},
    {"id": 2, "title": "Suspicious Login", "status": "Investigating"}
]

@app.route("/")
def home():
    return jsonify({"message": "Zerothurst SecureTrack API is running"})

@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(incidents)

@app.route("/incidents", methods=["POST"])
def add_incident():
    data = request.get_json()
    new_incident = {
        "id": len(incidents) + 1,
        "title": data.get("title", "Untitled Incident"),
        "status": data.get("status", "Open")
    }
    incidents.append(new_incident)
    return jsonify(new_incident), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
