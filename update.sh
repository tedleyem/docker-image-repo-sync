#!/bin/bash 
# Add timestamp to UPDATE.md file to trigger github actions.
 
# Define the file name
FILE="UPDATE.md"

# Get the current date in the format YYYY-MM-DD
CURRENT_DATE=$(date +"%Y-%m-%d")

# Get the current date and time in EST
TIMESTAMP=$(env TZ='America/New_York' date +"%Y-%m-%d %H:%M:%S %Z")

# Check if UPDATE.md exists, if not, create the file
if [ ! -f "$FILE" ]; then
  touch "$FILE"
fi

# Get the last line of the file
LAST_LINE=$(tail -n 1 "$FILE")

# Add timestamp to UPDATE.md
if [ "$LAST_LINE" == "$CURRENT_DATE" ]; then
  echo "$TIMESTAMP" >> "$FILE"
else
  echo "$CURRENT_DATE" >> "$FILE"
  echo "$TIMESTAMP" >> "$FILE"
fi

# Git PUSH
git add "$FILE"
git commit -m "sending push on $CURRENT_DATE"
git push

