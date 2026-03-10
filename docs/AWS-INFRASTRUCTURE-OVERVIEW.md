# AWS Infrastructure Overview

## Current State (March 10, 2026)

### Cost Summary
- **Current Monthly Cost:** ~$41/month
- **Projected with Bedrock Agent:** ~$25/month
- **Savings:** $16/month (40% reduction)

### Active Resources

#### Compute
| Resource | Type | Status | Monthly Cost |
|----------|------|--------|--------------|
| OpenClaw-JLT-Server | t3.xlarge | Running | $35.00 |
| Master-CMS-Serv-01 | t3.small | Stopped | $0.00 |

#### Storage
| Resource | Size | Type | Monthly Cost |
|----------|------|------|--------------|
| OpenClaw-JLT-Volume | 30 GB | gp3 | $2.40 |
| Old-Directus-Data | 8 GB | gp3 | $0.64 |
| Master-CMS volume | 8 GB | gp3 | $0.64 |

#### S3 Buckets
| Bucket | Purpose | Size | Monthly Cost |
|--------|---------|------|--------------|
| johnsonlegalteam-website | JLT website | ~5 MB | $0.00 |
| innercityyouthgroup-website | ICYG website | ~3 MB | $0.00 |
| mrtechfixes-com | MTF website | ~4 MB | $0.00 |
| agency2-saas-reviews | Agency2 website | ~2 MB | $0.00 |
| directus-cms-ui | CMS dashboard | ~1 MB | $0.00 |

#### CloudFront Distributions
| Distribution | Domain | Origin | Traffic |
|--------------|--------|--------|---------|
| EV61MLT5H1GGI | d39ck3l5w3yj0.cloudfront.net | JLT S3 | 48 req/mo |
| E1GF4URLG1CTTB | d29d5ogsimjcr6.cloudfront.net | ICYG S3 | ~0 req/mo |
| E25DZD0N0BGJG2 | d1gyg4o6kz0jap.cloudfront.net | MTF S3 | ~0 req/mo |
| E1YJFV9W0VK26B | d2gfwx5el5bwlu.cloudfront.net | Agency2 S3 | ~0 req/mo |

#### Networking
- VPC: vpc-08bcace0fc08e0fbf
- Subnet: subnet-0b841fe41becc2140
- Security Group: sg-0c8d9e41556ff4f63 (metrotec-strapi-sg)
- Monthly Cost: ~$2.20

### Services Running on OpenClaw Server

#### Docker Containers
- **Directus CMS:** Port 8055
- **Umami Analytics:** Port 3000
- **PostgreSQL 16:** Port 5432

#### Websites Tracked
- Johnson Legal Team (Umami ID: 18f91e4b-7106-454d-83ad-81ffd7f01e1b)
- Inner City Youth Group (not configured)
- Mr Tech Fixes (not configured)
- Agency2 SaaS Reviews (not configured)

### Traffic Analysis (Last 30 Days)
- **Total Requests:** 48
- **Unique Visitors:** 0 (tracking not installed)
- **Average Daily Requests:** 1.6
- **Conclusion:** Essentially zero real traffic

## Optimization Plan

### Phase 1: Downsize EC2 (Immediate)
**Action:** Resize OpenClaw-JLT-Server from t3.xlarge to t3.small
**Savings:** ~$20/month
**Steps:**
1. Stop instance
2. Change instance type
3. Start instance
4. Verify services running

### Phase 2: Deploy Bedrock Agent (Week 1)
**Action:** Create Bedrock Agent with action groups
**Cost:** +$5-10/month
**Net Savings:** ~$10-15/month
**Steps:**
1. Create Bedrock Agent
2. Deploy Lambda functions
3. Configure Gateway
4. Test workflows

### Phase 3: Cleanup (Week 2)
**Action:** Remove unused resources
**Savings:** ~$1/month
**Steps:**
1. Delete "Old-Directus-Data" volume (8 GB)
2. Terminate Master-CMS-Serv-01 instance
3. Remove unused snapshots

### Phase 4: Enable Monitoring (Week 2)
**Action:** Set up CloudWatch dashboards and alarms
**Cost:** $0 (within free tier)
**Steps:**
1. Create cost alert ($30 threshold)
2. Create agent failure alerts
3. Create server health dashboard

## Resource Cleanup Checklist

### Safe to Delete
- [ ] vol-07808c96371944e6c (Old-Directus-Data, 8 GB)
- [ ] i-07e46a6f6b8642d83 (Master-CMS-Serv-01, stopped)
- [ ] Old EBS snapshots (if any)

### Keep
- [x] i-0fad1494190159c10 (OpenClaw-JLT-Server)
- [x] vol-0c49f28aa42f72fcc (OpenClaw main volume, 30 GB)
- [x] All S3 buckets
- [x] All CloudFront distributions
- [x] VPC and networking

## Cost Tracking

### February 2026 (Partial)
- EC2 Compute: $7.09
- EC2 Other: $2.11
- S3: $0.00
- VPC: $0.27
- **Total:** $9.47 (19 days)

### March 2026 (10 days so far)
- EC2 Compute: $11.44
- EC2 Other: $3.08
- S3: $0.04
- VPC: $0.73
- CloudFront: $0.00
- **Total:** $15.29

### Projected March 2026
- **Current trajectory:** ~$45-50
- **After optimization:** ~$25-30

## Access Information

### EC2 Instances
- **OpenClaw Server:** 44.211.34.6
- **SSH Key:** metrotec2026.pem
- **User:** ubuntu

### Services
- **Directus:** http://44.211.34.6:8055
- **Umami:** http://44.211.34.6:3000
- **CMS Dashboard:** http://directus-cms-ui.s3-website-us-east-1.amazonaws.com

### Websites
- **JLT:** https://d39ck3l5w3yj0.cloudfront.net
- **ICYG:** https://d29d5ogsimjcr6.cloudfront.net
- **MTF:** https://d1gyg4o6kz0jap.cloudfront.net
- **Agency2:** https://d2gfwx5el5bwlu.cloudfront.net

## Security Notes

### Current Issues
- ⚠️ CloudFront logging disabled (no traffic audit trail)
- ⚠️ Umami tracking not installed on websites
- ⚠️ No Cognito authentication on CMS dashboard
- ⚠️ EBS volumes not encrypted

### Recommended Fixes
1. Enable CloudFront access logs
2. Install Umami tracking scripts
3. Implement Cognito auth on dashboard
4. Encrypt EBS volumes on next snapshot
5. Enable AWS Config for compliance

## Backup Strategy

### Current Backups
- EBS snapshots: Manual only
- Database: No automated backups
- S3: Versioning not enabled

### Recommended
1. Enable automated EBS snapshots (daily)
2. Set up PostgreSQL automated backups
3. Enable S3 versioning on website buckets
4. Store backups in separate region

## Disaster Recovery

### RTO (Recovery Time Objective)
- **Current:** 2-4 hours (manual restore)
- **Target:** 30 minutes (automated)

### RPO (Recovery Point Objective)
- **Current:** 24 hours (last manual backup)
- **Target:** 1 hour (automated snapshots)

### Recovery Steps
1. Launch new EC2 from latest snapshot
2. Attach EBS volume
3. Start Docker containers
4. Update DNS/CloudFront if needed
5. Verify services operational

## Next Steps

1. **Immediate:** Review and approve optimization plan
2. **This Week:** Downsize EC2 instance
3. **Next Week:** Deploy Bedrock Agent
4. **Ongoing:** Monitor costs and performance

## Related Documentation
- [Bedrock Agent Architecture](BEDROCK-AGENT-ARCHITECTURE.md)
- [OpenClaw Setup](OPENCLAW-SETUP.md)
- [Multi-Site CMS](MULTI-SITE-CMS-COMPLETE.md)
- [Umami Analytics](UMAMI-IMPLEMENTATION-COMPLETE.md)
