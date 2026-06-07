from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../frontend")
CORS(app)

incidents = [
    {"id": 1, "title": "Phishing Email", "severity": "High", "status": "Open"},
    {"id": 2, "title": "Suspicious Login", "severity": "Medium", "status": "Investigating"},
    {"id": 3, "title": "Malware Alert", "severity": "Critical", "status": "Open"}
]

@app.route("/")
def frontend_home():
    return send_from_directory("../frontend", "index.html")

@app.route("/dashboard")
def dashboard():
    return send_from_directory("../frontend", "dashboard.html")

@app.route("/login")
def login():
    return send_from_directory("../frontend", "login.html")

@app.route("/incidents-page")
def incidents_page():
    return send_from_directory("../frontend", "incidents.html")

@app.route("/reports")
def reports():
    return send_from_directory("../frontend", "reports.html")

@app.route("/settings")
def settings():
    return send_from_directory("../frontend", "settings.html")

@app.route("/api")
def api_home():
    return jsonify({"message": "Zerothurst SecureTrack API is running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(incidents)

@app.route("/incidents", methods=["POST"])
def add_incident():
    data = request.get_json()
    new_incident = {
        "id": len(incidents) + 1,
        "title": data.get("title", "Untitled Incident"),
        "severity": data.get("severity", "Medium"),
        "status": data.get("status", "Open")
    }
    incidents.append(new_incident)
    return jsonify(new_incident), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
