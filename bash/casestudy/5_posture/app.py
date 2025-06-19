from flask import Flask, jsonify, render_template
import yaml

app = Flask(__name__)

with open("signal-trust.yml", "r") as f:
    data = yaml.safe_load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/layers")
def get_layers():
    return jsonify(data["layers"])

@app.route("/layer/<name>")
def get_layer(name):
    for layer in data["layers"]:
        if layer["name"].lower() == name.lower():
            return jsonify(layer)
    return {"error": "Layer not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)

