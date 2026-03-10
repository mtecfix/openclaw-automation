#!/usr/bin/env python3
"""
DeepSeek Agent for OpenClaw
Handles automation tasks via DeepSeek API
"""
import os
import json
import sys
from datetime import datetime
from openai import OpenAI

# DeepSeek API configuration
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

# Agent system prompt
SYSTEM_PROMPT = """You are an intelligent automation agent for OpenClaw legal practice management system.

Your capabilities:
1. Process client intake forms from Johnson Legal Team website
2. Generate analytics reports from website traffic data
3. Update website content and manage CMS
4. Monitor infrastructure and alert on issues

When given a task:
- Analyze the request carefully
- Provide clear, actionable responses
- Format output as JSON when appropriate
- Log all actions taken

Available tools:
- upload_to_s3: Upload files to website buckets
- invalidate_cloudfront: Clear CDN cache
- get_metrics: Get traffic/server metrics
- send_email: Send notifications
- process_form: Extract form data

Respond concisely and professionally."""

def call_deepseek(prompt, conversation_history=None):
    """Call DeepSeek API"""
    if not DEEPSEEK_API_KEY:
        return "Error: DEEPSEEK_API_KEY not set"
    
    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL
    )
    
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    if conversation_history:
        messages.extend(conversation_history)
    
    messages.append({"role": "user", "content": prompt})
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7,
            max_tokens=2000
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error calling DeepSeek: {str(e)}"

def log_interaction(prompt, response):
    """Log agent interaction"""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'prompt': prompt,
        'response': response
    }
    
    with open('/var/log/deepseek-agent.log', 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

def main():
    if len(sys.argv) < 2:
        print("Usage: deepseek_agent.py 'your command'")
        sys.exit(1)
    
    prompt = ' '.join(sys.argv[1:])
    
    print(f"Processing: {prompt}\n")
    
    response = call_deepseek(prompt)
    
    print(response)
    
    log_interaction(prompt, response)

if __name__ == '__main__':
    main()
