# Bedrock Agent Architecture

## Overview
Intelligent AI agent system using AWS Bedrock AgentCore to automate website management, client intake, and infrastructure monitoring.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   User Interactions                      │
│  (Website forms, Dashboard commands, Scheduled tasks)    │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│            OpenClaw Server (t3.small)                    │
│  - Monitors events (forms, schedules, alerts)            │
│  - Issues commands to Bedrock Agent                      │
│  - Logs all agent actions                                │
│  - Fallback/retry logic                                  │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│         AWS Bedrock Agent (Serverless)                   │
│  Model: Claude 3.5 Sonnet                                │
│  Runtime: On-demand execution                            │
│  Memory: Persistent across sessions                      │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
┌───────▼──────┐ ┌──▼──────┐ ┌──▼──────────┐
│   Action     │ │ Action  │ │   Action    │
│   Group 1    │ │ Group 2 │ │   Group 3   │
│              │ │         │ │             │
│ CMS Mgmt     │ │Analytics│ │ Client      │
│ - Directus   │ │ - Umami │ │ Intake      │
│ - S3 Upload  │ │ - CloudW│ │ - OpenClaw  │
│ - CloudFront │ │ - Reports│ │ - Email     │
└──────────────┘ └─────────┘ └─────────────┘
```

## Components

### 1. OpenClaw Server (Control Center)
**Instance:** EC2 t3.small (2 vCPU, 4GB RAM)
**Cost:** ~$15/month
**Role:** Monitoring & orchestration

**Responsibilities:**
- Run cron jobs for scheduled tasks
- Monitor website form submissions
- Detect infrastructure issues
- Invoke Bedrock Agent with commands
- Log all agent activities
- Retry failed operations

### 2. Bedrock Agent (AI Worker)
**Service:** AWS Bedrock AgentCore
**Model:** Claude 3.5 Sonnet
**Cost:** ~$5-10/month (pay per use)
**Role:** Task execution

**Capabilities:**
- Natural language understanding
- Multi-step task execution
- Code generation & execution
- Web browsing
- API integrations
- Persistent memory

### 3. Action Groups (Tools)

#### Action Group 1: CMS Management
**Lambda Functions:**
- `update-directus-content` - Modify CMS content
- `upload-to-s3` - Upload files to website buckets
- `invalidate-cloudfront` - Clear CDN cache
- `generate-content` - AI content generation

#### Action Group 2: Analytics & Reporting
**Lambda Functions:**
- `get-umami-stats` - Fetch website analytics
- `get-cloudwatch-metrics` - Infrastructure metrics
- `generate-report` - Create summary reports
- `send-email-report` - Email via SES

#### Action Group 3: Client Intake
**Lambda Functions:**
- `process-form-submission` - Parse intake forms
- `create-openclaw-case` - Create case in OpenClaw
- `extract-case-details` - AI extraction from forms
- `send-confirmation` - Email client confirmation

## Workflows

### Workflow 1: Client Intake Automation
```
1. User submits form on JLT website
2. Form data stored in S3 trigger
3. OpenClaw server detects new submission
4. OpenClaw invokes Bedrock Agent:
   - Task: "Process personal injury intake form #12345"
5. Agent executes:
   - Reads form data from S3
   - Extracts: client name, incident details, damages
   - Creates case in OpenClaw API
   - Generates case summary
   - Sends confirmation email to client
   - Sends alert to attorney
6. Agent reports back to OpenClaw
7. OpenClaw logs completion
```

### Workflow 2: Daily Analytics Report
```
1. OpenClaw cron job triggers at 9:00 AM
2. OpenClaw invokes Bedrock Agent:
   - Task: "Generate daily analytics report"
3. Agent executes:
   - Queries Umami for all 4 sites
   - Queries CloudWatch for server metrics
   - Analyzes traffic patterns
   - Generates summary report
   - Emails report to admin
4. Agent stores report in S3
5. OpenClaw logs completion
```

### Workflow 3: Content Update
```
1. Admin sends command via dashboard
2. OpenClaw receives: "Add blog post about expungements"
3. OpenClaw invokes Bedrock Agent:
   - Task: "Create and publish blog post on expungements"
4. Agent executes:
   - Generates blog content using Claude
   - Creates HTML page
   - Uploads to S3 bucket
   - Invalidates CloudFront cache
   - Updates sitemap
5. Agent confirms: "Published at /blog/expungements"
6. OpenClaw logs completion
```

### Workflow 4: Infrastructure Monitoring
```
1. OpenClaw monitors every 15 minutes
2. Detects: High CPU usage on EC2
3. OpenClaw invokes Bedrock Agent:
   - Task: "Investigate high CPU usage"
4. Agent executes:
   - Checks CloudWatch metrics
   - Reviews recent logs
   - Identifies process causing issue
   - Generates diagnostic report
   - Sends alert if critical
5. Agent recommends action
6. OpenClaw logs findings
```

## Security

### IAM Roles
- **OpenClaw Server Role:** Invoke Bedrock, read CloudWatch, read S3
- **Bedrock Agent Role:** Execute Lambda, read/write S3, access Directus
- **Lambda Execution Roles:** Minimal permissions per function

### Network Security
- OpenClaw server in private subnet
- Bedrock Agent uses VPC endpoints
- All API calls over HTTPS
- No public access to Directus

### Data Protection
- Form data encrypted at rest (S3)
- Agent memory encrypted
- Secrets in AWS Secrets Manager
- Audit logs in CloudWatch

## Cost Breakdown

| Component | Monthly Cost |
|-----------|--------------|
| EC2 t3.small (OpenClaw) | $15.00 |
| EBS 30GB gp3 | $2.40 |
| Bedrock Agent runtime | $5-10.00 |
| Lambda executions | $0.50 |
| S3 storage | $0.12 |
| CloudFront | $0.00 |
| VPC/Networking | $2.00 |
| **TOTAL** | **$25-30/month** |

**Savings vs current:** $15-20/month (40% reduction)

## Monitoring

### CloudWatch Dashboards
- Agent invocation count
- Agent execution time
- Lambda errors
- EC2 metrics
- Cost tracking

### Alerts
- Agent failures (SNS)
- High costs (Budget alerts)
- Server issues (CloudWatch alarms)
- Form submission errors

## Deployment Steps

1. **Downsize EC2 instance** (t3.xlarge → t3.small)
2. **Create Bedrock Agent** with Claude 3.5 Sonnet
3. **Deploy Lambda functions** for action groups
4. **Configure Agent Gateway** to connect tools
5. **Set up Agent Memory** for context persistence
6. **Configure Agent Policies** for access control
7. **Deploy monitoring scripts** on OpenClaw server
8. **Test workflows** end-to-end
9. **Enable production monitoring**
10. **Document runbooks**

## Maintenance

### Daily
- Review agent execution logs
- Check error rates
- Monitor costs

### Weekly
- Review agent performance metrics
- Optimize slow operations
- Update agent instructions if needed

### Monthly
- Analyze cost trends
- Review security logs
- Update Lambda functions
- Test disaster recovery

## Future Enhancements

- **Multi-agent system:** Specialized agents per website
- **Voice interface:** Call OpenClaw to issue commands
- **Predictive analytics:** Agent predicts traffic/issues
- **Auto-scaling:** Agent adjusts resources based on load
- **Legal research:** Agent browses case law for attorneys

## Related Documentation
- [OpenClaw Setup](OPENCLAW-SETUP.md)
- [Directus CMS](MULTI-SITE-CMS-COMPLETE.md)
- [Umami Analytics](UMAMI-IMPLEMENTATION-COMPLETE.md)
- [AWS Cost Optimization](AWS-COST-ANALYSIS.md)
