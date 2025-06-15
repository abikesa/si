#!/bin/bash

declare -a EMOJIS=("🌊" "❤️" "🌀" "🐬" "🔁")
declare -a NAMES=("GitHub" "Project" "Fork" "Branch" "Recurse")
declare -a FUNCTIONS=("Origin Pool" "Pulse of Purpose" "Sacred Divergence" "Playful Hypothesis" "Return Loop")
declare -a PHILOSOPHERS=("Bacon" "Hume" "Aquinas" "Kant" "Nietzsche")
declare -a STAGES=("Ukuvula" "Ukuzula" "Ukusoma" "Ukubona" "Ukuvela")
declare -a TOOLS=("Clone" "Init" "Fork" "Branch" "Merge")
declare -a QUOTES=(
  "All code flows from the sea of forks."
  "Without intent, there is no commit."
  "To fork is to bless your own path."
  "Branch boldly, as if the universe itself were rebasing."
  "Every merge is eternal recurrence."
)

i=$(( RANDOM % 5 ))

echo ""
echo "${EMOJIS[$i]}  ${NAMES[$i]} — ${FUNCTIONS[$i]}"
echo "Tool: ${TOOLS[$i]}"
echo "Philosopher: ${PHILOSOPHERS[$i]} | Stage: ${STAGES[$i]}"
echo "💬 \"${QUOTES[$i]}\""

# Optional: Add files before committing
git add .

# Commit with spiral message
git commit -m "${EMOJIS[$i]} ${NAMES[$i]}: ${QUOTES[$i]}"


