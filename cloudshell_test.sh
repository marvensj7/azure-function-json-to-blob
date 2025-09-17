#!/bin/bash
# Azure Cloud Shell test script for the HTTP-triggered Azure Function

# Replace these with your actual function URL and key
FUNCTION_URL="<YOUR_FUNCTION_URL>/api/write2blob"
FUNCTION_KEY="<YOUR_FUNCTION_KEY>"

# Sample JSON payload
cat <<EOF > sample.json
{
  "username": "testuser",
  "score": 99,
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF

# Trigger the function and display the result
curl -X POST "$FUNCTION_URL?code=$FUNCTION_KEY" \
  -H "Content-Type: application/json" \
  -d @sample.json | tee evidence/successful_run.json