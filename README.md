# OpenClaw Automation

AI-powered automation system for legal practice management using DeepSeek and AWS.

## Overview

Intelligent agent that automates:
- Client intake processing
- Website analytics reporting
- Content management
- Infrastructure monitoring

## Architecture

```
DeepSeek Agent (OpenClaw Server)
    ↓
Lambda Functions (AWS)
    ↓
Services (S3, CloudFront, SES, CloudWatch)
```

## Components

### Agent
- **DeepSeek API** - AI intelligence
- **Python script** - Runs on OpenClaw server
- **Cost:** $1-2/month

### Lambda Functions (5)
- `openclaw-upload-to-s3` - Upload files to websites
- `openclaw-invalidate-cloudfront` - Clear CDN cache
- `openclaw-get-cloudwatch-metrics` - Get traffic data
- `openclaw-send-email` - Send notifications
- `openclaw-process-form` - Extract form data

### Infrastructure
- **EC2:** t3.small (2 vCPU, 2GB RAM)
- **Services:** Directus CMS, Umami Analytics, PostgreSQL
- **Websites:** 4 static sites on S3 + CloudFront

## Cost

| Component | Monthly |
|-----------|---------|
| EC2 t3.small | $15.00 |
| EBS 30GB | $2.40 |
| DeepSeek API | $1-2.00 |
| Lambda | $0.50 |
| S3 + CloudFront | $0.12 |
| VPC | $2.00 |
| **Total** | **$21-22/month** |

**Savings:** 46% vs original setup

## Setup

### 1. Get DeepSeek API Key
```bash
# Sign up at https://platform.deepseek.com/
# Create API key
# Set on server:
export DEEPSEEK_API_KEY='your-key-here'
```

### 2. Deploy Agent
```bash
# On OpenClaw server
scp agent/deepseek_agent.py ubuntu@100.56.11.242:/usr/local/bin/
chmod +x /usr/local/bin/deepseek_agent.py
```

### 3. Deploy Lambda Functions
```bash
# Package and deploy
cd lambda
for func in *.py; do
  zip ${func%.py}.zip $func
  aws lambda update-function-code \
    --function-name openclaw-${func%.py} \
    --zip-file fileb://${func%.py}.zip
done
```

## Usage

### Test Agent
```bash
/usr/local/bin/deepseek_agent.py "Hello! Confirm operational status."
```

### Process Intake Form
```bash
/usr/local/bin/deepseek_agent.py "Process intake: Name: John Smith, Case: Personal Injury"
```

### Generate Report
```bash
/usr/local/bin/deepseek_agent.py "Generate daily analytics report for all websites"
```

### Update Content
```bash
/usr/local/bin/deepseek_agent.py "Write a blog post about expungement law"
```

## Automation

### Cron Jobs
```bash
# Daily report at 9 AM
0 9 * * * /usr/local/bin/deepseek_agent.py "Generate daily report"

# Check forms every 5 minutes
*/5 * * * * /usr/local/bin/check_forms.sh
```

## Development

### Local Setup
```bash
git clone https://github.com/mtecfix/openclaw-automation.git
cd openclaw-automation
pip install -r requirements.txt
```

### Deploy
```bash
git add .
git commit -m "Update agent"
git push origin main

# On server
cd /opt/openclaw-automation
git pull
```

## Documentation

- [DeepSeek Agent Setup](docs/DEEPSEEK-AGENT-SETUP.md)
- [Deployment Guide](docs/DEPLOYMENT-COMPLETE.md)
- [AWS Infrastructure](docs/AWS-INFRASTRUCTURE-OVERVIEW.md)
- [Lambda Functions](docs/LAMBDA-FUNCTIONS-DEPLOYED.md)
- [Architecture](docs/BEDROCK-AGENT-ARCHITECTURE.md)

## Websites Managed

1. **Johnson Legal Team** - d39ck3l5w3yj0.cloudfront.net
2. **Inner City Youth Group** - d29d5ogsimjcr6.cloudfront.net
3. **Mr Tech Fixes** - d1gyg4o6kz0jap.cloudfront.net
4. **Agency2 SaaS Reviews** - d2gfwx5el5bwlu.cloudfront.net

## Server

- **IP:** 100.56.11.242
- **SSH:** `ssh -i metrotec2026.pem ubuntu@100.56.11.242`
- **Logs:** `/var/log/deepseek-agent.log`

## License

MIT

## Author

mtecfix
# Auto-deploy test
