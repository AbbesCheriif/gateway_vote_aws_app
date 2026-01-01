from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

VOTE_MGMT_URL = "http://10.100.20.139:5001"

@app.route("/projects")
def projects():
    return requests.get(f"{VOTE_MGMT_URL}/projects").json()
    # static_projects = [
    #     {
    #         "id": 1,
    #         "name": "Projet Alpha",
    #         "logo_url": "https://via.placeholder.com/80?text=Alpha"
    #     },
    #     {
    #         "id": 2,
    #         "name": "Projet Beta",
    #         "logo_url": "https://via.placeholder.com/80?text=Beta"
    #     },
    #     {
    #         "id": 3,
    #         "name": "Projet Gamma",
    #         "logo_url": "https://via.placeholder.com/80?text=Gamma"
    #     }
    # ]
    # return jsonify(static_projects)

@app.route("/vote", methods=["POST"])
def vote():
    # API publique (via NAT)
    # ip_info = requests.get("http://ip-api.com/json").json()
    # if ip_info.get("country") != "France":
    #     return jsonify({"error": "Vote refusé"}), 403

    return requests.post(f"{VOTE_MGMT_URL}/vote", json=request.json).json()

app.run(host="0.0.0.0", port=5000)
