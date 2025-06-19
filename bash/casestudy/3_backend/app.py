from flask import Flask, jsonify
import yaml

app = Flask(__name__)

with open("signal-trust.yml", "r") as f:
    data = yaml.safe_load(f)

@app.route("/layers", methods=["GET"])
def get_layers():
    return jsonify(data["layers"])

@app.route("/layer/<name>", methods=["GET"])
def get_layer(name):
    for layer in data["layers"]:
        if layer["name"].lower() == name.lower():
            return jsonify(layer)
    return {"error": "Layer not found"}, 404

