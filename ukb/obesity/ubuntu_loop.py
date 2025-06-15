from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

UBUNTU_MAP = {
    "ukuvula": {
        "emoji": "🌊",
        "keywords": ["anxious", "stress", "beginning", "alert", "fight", "flight", "tense"],
        "poem": "The opening hum. Cortisol sings the minor key of readiness. The bone remembers the storm."
    },
    "ukuzula": {
        "emoji": "❤️",
        "keywords": ["hunger", "search", "wander", "explore", "seek", "curious", "touch"],
        "poem": "The wandering. Sensory drift. Joints bend toward communion. The hunger to connect."
    },
    "ukusoma": {
        "emoji": "🌀",
        "keywords": ["fledgling", "potential", "paused", "sus", "waiting", "ready", "tense"],
        "poem": "The fledgling moment. Suspended potential. Muscles brace as gospel chords hover, unresolved."
    },
    "ukubona": {
        "emoji": "🐬",
        "keywords": ["see", "insight", "perceive", "learn", "witness", "aha", "memory"],
        "poem": "Perception as prayer. The hippocampus prunes. Memory is mercy. The dolphin flips and learns."
    },
    "ukuvela": {
        "emoji": "🔁",
        "keywords": ["emerge", "release", "obesity", "collapse", "move", "ritual", "return"],
        "poem": "Emergence. Obesity as accumulated unresolveds. Release as return. Activity becomes ritual."
    }
}

def detect_stage(user_input):
    text = user_input.lower()
    for stage, data in UBUNTU_MAP.items():
        if any(keyword in text for keyword in data["keywords"]):
            return stage, data
    return "unknown", {
        "emoji": "❓",
        "poem": "Unrecognized input. Perhaps you’re between loops — the silence before the song?"
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stage", methods=["POST"])
def get_stage():
    user_input = request.json.get("input", "")
    stage, data = detect_stage(user_input)
    return jsonify({
        "stage": stage,
        "emoji": data["emoji"],
        "description": data["poem"]
    })

if __name__ == "__main__":
    app.run(debug=True)

