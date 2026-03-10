# Lambda Functions Deployed

## Day 5-7 Complete: Lambda Action Groups Created ✓

### Functions Deployed (5)

| Function Name | Purpose | ARN |
|---------------|---------|-----|
| openclaw-upload-to-s3 | Upload content to S3 | arn:aws:lambda:us-east-1:074126659776:function:openclaw-upload-to-s3 |
| openclaw-invalidate-cloudfront | Clear CDN cache | arn:aws:lambda:us-east-1:074126659776:function:openclaw-invalidate-cloudfront |
| openclaw-get-cloudwatch-metrics | Get traffic metrics | arn:aws:lambda:us-east-1:074126659776:function:openclaw-get-cloudwatch-metrics |
| openclaw-send-email | Send emails via SES | arn:aws:lambda:us-east-1:074126659776:function:openclaw-send-email |
| openclaw-process-form | Process intake forms | arn:aws:lambda:us-east-1:074126659776:function:openclaw-process-form |

### IAM Role

**Role:** OpenClawLambdaExecutionRole  
**ARN:** arn:aws:iam::074126659776:role/OpenClawLambdaExecutionRole

**Permissions:**
- S3: Read/Write to all website buckets
- CloudFront: Create invalidations
- CloudWatch: Read metrics
- SES: Send emails
- CloudWatch Logs: Write logs

### Action Group Schema

OpenAPI 3.0 schema created at: `/tmp/action-group-schema.json`

**Operations:**
1. `uploadToS3` - Upload files to website buckets
2. `invalidateCloudFront` - Clear CDN cache
3. `getCloudWatchMetrics` - Get traffic data
4. `sendEmail` - Send notifications
5. `processForm` - Extract form data

### Next Steps

**To register action group with Bedrock Agent:**

```bash
aws bedrock-agent create-agent-action-group \
  --agent-id 5X840PSSY1 \
  --agent-version DRAFT \
  --action-group-name "cms-management" \
  --action-group-executor '{"lambda":"arn:aws:lambda:us-east-1:074126659776:function:openclaw-upload-to-s3"}' \
  --api-schema file:///tmp/action-group-schema.json \
  --region us-east-1
```

**Note:** Umami stats function (get-umami-stats) requires `requests` library. Will be added via Lambda layer or deployed separately.

### Testing

Test individual functions:

```bash
# Test upload
aws lambda invoke \
  --function-name openclaw-upload-to-s3 \
  --payload '{"bucket":"johnsonlegalteam-website","key":"test.html","content":"<h1>Test</h1>"}' \
  /tmp/response.json

# Test CloudFront invalidation
aws lambda invoke \
  --function-name openclaw-invalidate-cloudfront \
  --payload '{"distributionId":"EV61MLT5H1GGI","paths":["/*"]}' \
  /tmp/response.json

# Test metrics
aws lambda invoke \
  --function-name openclaw-get-cloudwatch-metrics \
  --payload '{"distributionId":"EV61MLT5H1GGI","days":30}' \
  /tmp/response.json
```

### Cost Impact

**Lambda Costs:**
- Free tier: 1M requests/month, 400,000 GB-seconds compute
- Expected usage: ~1,000 invocations/month
- **Cost: $0.00-0.50/month** (within free tier)

**Total Monthly Cost:**
- EC2 t3.small: $15.00
- EBS 30GB: $2.40
- Bedrock Agent: $5-10.00
- Lambda: $0.50
- **Total: $22.90-27.90/month**

### Status

- ✓ EC2 downsized to t3.small
- ✓ Bedrock Agent created (5X840PSSY1)
- ✓ Lambda functions deployed (5)
- ✓ IAM roles configured
- ⏳ Action group registration (next)
- ⏳ OpenClaw integration (Day 8-9)

### Related Files

- Lambda functions: `/tmp/*.py`
- Function packages: `/tmp/*.zip`
- OpenAPI schema: `/tmp/action-group-schema.json`
- Test Lambda: `/tmp/test_agent_lambda.py`
