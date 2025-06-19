# 🌀 YAML Stack Demo – Signal–Trust

This is a five-layered system built around a single `signal-trust.yml` file that serves as the canonical source of meaning.

## 📂 Structure

| File | Role |
|------|------|
| `signal-trust.yml` | Source: Canonical data |
| `app.py` | API: Serve YAML as JSON |
| `templates/index.html` | UI: Render YAML visually |
| `static/style.css` | Optional styling |
| `yaml-stack.md` | Symbolic documentation |
| `README.md` | Meta-description, loop context |

## 🔁 Usage

```bash
pip install flask pyyaml
python app.py

