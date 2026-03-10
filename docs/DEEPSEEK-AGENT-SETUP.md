# DeepSeek Agent Setup

## Deployment Complete ✓

**Agent installed:** `/usr/local/bin/deepseek_agent.py`  
**Log file:** `/var/log/deepseek-agent.log`  
**Dependencies:** openai library (v2.26.0)

## Get DeepSeek API Key

1. Go to: https://platform.deepseek.com/
2. Sign up / Log in
3. Navigate to: API Keys
4. Create new API key
5. Copy the key

## Configure API Key

On OpenClaw server:

```bash
ssh -i ~/.ssh/metrotec2026.pem ubuntu@100.56.11.242

# Set API key (temporary)
export DEEPSEEK_API_KEY='your-api-key-here'

# Or set permanently
echo 'export DEEPSEEK_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Test Agent

```bash
# Simple test
/usr/local/bin/deepseek_agent.py "Hello! Confirm you are operational."

# Analytics report
/usr/local/bin/deepseek_agent.py "Generate a summary of website traffic for the last 30 days"

# Content generation
/usr/local/bin/deepseek_agent.py "Write a blog post about expungement law in 200 words"
```

## Usage Examples

### 1. Process Client Intake
```bash
/usr/local/bin/deepseek_agent.py "Process intake form: Name: John Smith, Case: Personal Injury, Details: Car accident on I-95"
```

### 2. Generate Report
```bash
/usr/local/bin/deepseek_agent.py "Create daily analytics report for all 4 websites"
```

### 3. Content Update
```bash
/usr/local/bin/deepseek_agent.py "Write a professional bio for attorney specializing in criminal defense"
```

### 4. Infrastructure Check
```bash
/usr/local/bin/deepseek_agent.py "Check server health and report any issues"
```

## Automated Workflows

Create cron jobs for scheduled tasks:

```bash
# Edit crontab
crontab -e

# Daily report at 9 AM
0 9 * * * /usr/local/bin/deepseek_agent.py "Generate daily analytics report" | mail -s "Daily Report" mrtechfixes.ai@gmail.com

# Check for new forms every 5 minutes
*/5 * * * * /usr/local/bin/check_forms.sh
```

## Integration with Lambda

The agent can trigger Lambda functions for actual operations:

```python
# Example: Agent decides to upload content
response = deepseek_agent.py "Generate homepage content"
# Then call Lambda to upload
aws lambda invoke --function-name openclaw-upload-to-s3 ...
```

## Cost Comparison

### DeepSeek API
- Input: $0.14 per 1M tokens
- Output: $0.28 per 1M tokens
- **Estimated: $1-2/month**

### AWS Bedrock (Claude)
- Input: $3.00 per 1M tokens
- Output: $15.00 per 1M tokens
- **Estimated: $5-10/month**

**Savings: $3-8/month using DeepSeek**

## Final Cost Summary

| Component | Monthly Cost |
|-----------|--------------|
| EC2 t3.small | $15.00 |
| EBS 30GB | $2.40 |
| DeepSeek API | $1-2.00 |
| Lambda | $0.50 |
| S3 | $0.12 |
| VPC | $2.00 |
| **Total** | **$21-22/month** |

**Total Savings: $19-20/month (46% reduction)**

## Monitoring

View agent logs:
```bash
tail -f /var/log/deepseek-agent.log
```

Check recent activity:
```bash
tail -20 /var/log/deepseek-agent.log | jq .
```

## Next Steps

1. Get DeepSeek API key
2. Configure on server
3. Test agent
4. Create automation scripts
5. Set up cron jobs

## Architecture

```
OpenClaw Server (100.56.11.242)
    ↓ calls
DeepSeek API (deepseek-chat model)
    ↓ returns instructions
OpenClaw Server
    ↓ executes via
Lambda Functions (5)
    ↓ interact with
AWS Services (S3, CloudFront, SES, CloudWatch)
```

## Support

- DeepSeek Docs: https://platform.deepseek.com/docs
- API Status: https://status.deepseek.com
- Pricing: https://platform.deepseek.com/pricing

## Files

- Agent: `/usr/local/bin/deepseek_agent.py`
- Logs: `/var/log/deepseek-agent.log`
- Lambda functions: AWS Lambda console
- Documentation: `/mnt/c/Users/admin/*.md`
