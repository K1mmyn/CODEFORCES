#!/bin/bash

# Check if a filename/message was provided
if [ -z "$1" ]; then
  echo "Error: Please provide a commit message (e.g., ./push.sh my_file.txt)"
  exit 1
fi

# Stage all changes
git add .

# Commit with the provided argument as the message
git commit -m "$1"

# Push to the current branch
git push
