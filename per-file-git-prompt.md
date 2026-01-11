# Per-File Git Add/Commit/Push Prompt

Use this prompt in your terminal to add, commit, and push each file in a folder one-by-one on the **current branch**, with defensive checks and clear failures.

---

## Preconditions
- You are already on the correct branch (current branch will be used).
- Remote is configured and authenticated (`git remote -v` works).
- Only the target folder has changes you intend to push.
- You will manually replace `FOLDER_PATH_HERE` with your folder (example: `structural/day5`).

---

## Prompt to Run (copy-paste)
```bash
set -euo pipefail

folder="FOLDER_PATH_HERE"       # e.g., structural/day5
repo="/home/deepak/Desktop/DATA ENGINEERING PYTHON"

cd "$repo" || { echo "Repo path invalid"; exit 1; }

# Basic safety checks
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo "Not a git repo"; exit 1; }
git remote -v | grep -q . || { echo "No git remote configured"; exit 1; }
[ -d "$folder" ] || { echo "Folder not found: $folder"; exit 1; }

shopt -s nullglob
files=("$folder"/*)
[ ${#files[@]} -gt 0 ] || { echo "No files in folder"; exit 0; }

for f in "${files[@]}"; do
  [ -f "$f" ] || { echo "Skip (not a file): $f"; continue; }

  # Skip if no changes for this file
  if git diff --quiet -- "$f" && git diff --cached --quiet -- "$f"; then
    echo "No changes: $f";
    continue;
  fi

  echo "Processing: $f"
  git add -- "$f" || { echo "git add failed: $f"; break; }
  git commit -m "Update $(basename "$f")" || { echo "git commit failed: $f"; break; }
  git push || { echo "git push failed after committing $f"; break; }
  echo "Pushed: $f"
done
```

---

## Notes
- Handles files with spaces because paths are quoted.
- Skips directories; only processes regular files.
- Skips clean files (no staged or unstaged changes).
- Stops on first failure and reports which step failed.
- Adjust the commit message pattern if desired.
- Other modified files outside the folder are untouched; commit them separately.
