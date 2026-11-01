#!/usr/bin/env bash
set -euo pipefail

OWNER="aKmsdfhjb"
REPOS=(
  "Chatbot"
  "Doodle"
  "Pneumonia-COVID-Detection-CNN"
  "Caesar-Cipher"
  "python-rpg_character-generator"
  "poem-pin-extractor"
  "REVIEW_RATINGS_CLASSIFIER"
  "Wedding_invite"
  "Smart-parking-solution"
  "Sentiment-Analysis-Model-Comparison"
  "Ai-quiz-and-notes"
  "Study-patner"
  "Portfoilo"
  "anything"
)

command -v gh >/dev/null || { echo "Install GitHub CLI (gh) first."; exit 1; }
gh auth status >/dev/null || { echo "Authenticate with: gh auth login"; exit 1; }

GH_USER="$(gh api user --jq .login)"
GH_ID="$(gh api user --jq .id)"
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

for REPO in "${REPOS[@]}"; do
  echo "Publishing wiki pages for $OWNER/$REPO"
  gh repo clone "$OWNER/$REPO" "$WORKDIR/$REPO-source" -- --quiet

  if ! git clone "https://github.com/$OWNER/$REPO.wiki.git" "$WORKDIR/$REPO-wiki" 2>/dev/null; then
    echo "  SKIP: Wiki is not enabled or is not accessible. Enable it in repository settings first."
    continue
  fi

  mkdir -p "$WORKDIR/$REPO-wiki"
  cp "$WORKDIR/$REPO-source/docs/wiki/"*.md "$WORKDIR/$REPO-wiki/"
  git -C "$WORKDIR/$REPO-wiki" add Home.md Architecture.md

  if git -C "$WORKDIR/$REPO-wiki" diff --cached --quiet; then
    echo "  No wiki changes."
  else
    git -C "$WORKDIR/$REPO-wiki" config user.name "$GH_USER"
    git -C "$WORKDIR/$REPO-wiki" config user.email "$GH_ID+$GH_USER@users.noreply.github.com"
    git -C "$WORKDIR/$REPO-wiki" commit -m "Publish project wiki pages"
    git -C "$WORKDIR/$REPO-wiki" push
  fi
done

echo "Wiki publishing pass complete."
