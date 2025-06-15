from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

spiral = [
    {
        "emoji": "🌊", "name": "GitHub", "function": "Origin Pool",
        "philosopher": "Bacon", "stage": "Ukuvula", "tool": "Clone",
        "quote": "All code flows from the sea of forks."
    },
    {
        "emoji": "❤️", "name": "Project", "function": "Pulse of Purpose",
        "philosopher": "Hume", "stage": "Ukuzula", "tool": "Init",
        "quote": "Without intent, there is no commit."
    },
    {
        "emoji": "🌀", "name": "Fork", "function": "Sacred Divergence",
        "philosopher": "Aquinas", "stage": "Ukusoma", "tool": "Fork",
        "quote": "To fork is to bless your own path."
    },
    {
        "emoji": "🐬", "name": "Branch", "function": "Playful Hypothesis",
        "philosopher": "Kant", "stage": "Ukubona", "tool": "Branch",
        "quote": "Branch boldly, as if the universe itself were rebasing."
    },
    {
        "emoji": "🔁", "name": "Recurse", "function": "Return Loop",
        "philosopher": "Nietzsche", "stage": "Ukuvela", "tool": "Merge",
        "quote": "Every merge is eternal recurrence."
    }
]

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>Inferential Git Spiral</title>
      <style>
        body { background: #111; color: #fff; font-family: monospace; text-align: center; padding-top: 5em; }
        button { background: #222; color: #0ff; border: 2px solid #0ff; padding: 1em 2em; font-size: 1.2em; cursor: pointer; }
        .result { margin-top: 2em; font-size: 1.5em; line-height: 1.6em; }
        .emoji { font-size: 3em; }
      </style>
    </head>
    <body>
      <h1>🧙 Inferential Git Spiral</h1>
      <button onclick="spin()">Spin the Spiral</button>
      <div class="result" id="result"></div>

      <script>
        async function spin() {
          const res = await fetch('/roll');
          const stage = await res.json();
          document.getElementById('result').innerHTML = `
            <div class="emoji">${stage.emoji}</div>
            <div><strong>${stage.name}</strong> — <em>${stage.function}</em></div>
            <div>Tool: ${stage.tool}</div>
            <div>Philosopher: ${stage.philosopher}</div>
            <div>Stage: ${stage.stage}</div>
            <blockquote>“${stage.quote}”</blockquote>
          `;
        }
      </script>
    </body>
    </html>
    """)

@app.route('/roll')
def roll_spiral():
    return jsonify(random.choice(spiral))

if __name__ == '__main__':
    app.run(debug=True)

