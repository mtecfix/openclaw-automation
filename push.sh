#!/bin/bash
echo "=== GitHub Authentication ==="
gh auth login

echo ""
echo "=== Creating Repo and Pushing ==="
gh repo create openclaw-automation --public --source=. --remote=origin --push

echo ""
echo "✅ Done! Repo live at: https://github.com/mtecfix/openclaw-automation"
