#!/bin/bash
# Deploy script for OpenClaw server

SERVER="ubuntu@100.56.11.242"
KEY="~/.ssh/metrotec2026.pem"

echo "Deploying agent to OpenClaw server..."

# Deploy agent
scp -i $KEY agent/deepseek_agent.py $SERVER:/tmp/
ssh -i $KEY $SERVER "sudo mv /tmp/deepseek_agent.py /usr/local/bin/ && sudo chmod +x /usr/local/bin/deepseek_agent.py"

echo "Agent deployed successfully!"
echo "Test with: ssh -i $KEY $SERVER '/usr/local/bin/deepseek_agent.py \"Hello\"'"
