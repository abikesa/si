import random

spiral = [
    {
        "emoji": "🌊",
        "name": "GitHub",
        "function": "Origin Pool",
        "philosopher": "Bacon",
        "stage": "Ukuvula",
        "tool": "Clone",
        "quote": "All code flows from the sea of forks."
    },
    {
        "emoji": "❤️",
        "name": "Project",
        "function": "Pulse of Purpose",
        "philosopher": "Hume",
        "stage": "Ukuzula",
        "tool": "Init",
        "quote": "Without intent, there is no commit."
    },
    {
        "emoji": "🌀",
        "name": "Fork",
        "function": "Sacred Divergence",
        "philosopher": "Aquinas",
        "stage": "Ukusoma",
        "tool": "Fork",
        "quote": "To fork is to bless your own path."
    },
    {
        "emoji": "🐬",
        "name": "Branch",
        "function": "Playful Hypothesis",
        "philosopher": "Kant",
        "stage": "Ukubona",
        "tool": "Branch",
        "quote": "Branch boldly, as if the universe itself were rebasing."
    },
    {
        "emoji": "🔁",
        "name": "Recurse",
        "function": "Return Loop",
        "philosopher": "Nietzsche",
        "stage": "Ukuvela",
        "tool": "Merge",
        "quote": "Every merge is eternal recurrence."
    }
]

def invoke_git_spiral():
    stage = random.choice(spiral)
    print(f"\n{stage['emoji']} {stage['name']} — {stage['function']}")
    print(f"Tool: {stage['tool']}")
    print(f"Philosopher: {stage['philosopher']} | Stage: {stage['stage']}")
    print(f"Quote: \"{stage['quote']}\"\n")

if __name__ == "__main__":
    print("🎰 Spinning the Inferential Git Spiral...\n")
    invoke_git_spiral()

