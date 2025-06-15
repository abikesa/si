from flask import Flask, render_template
import yaml

app = Flask(__name__)

def load_data():
    with open('data.yml', 'r') as f:
        return yaml.safe_load(f)

@app.route('/')
def index():
    data = load_data()
    layers = data.get('spiral_layers', [])
    return render_template('index.html', layers=layers)

if __name__ == '__main__':
    app.run(debug=True)
