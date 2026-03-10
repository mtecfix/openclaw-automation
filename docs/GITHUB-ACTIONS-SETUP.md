# GitHub Actions Setup

## Auto-Deploy Configured ✓

Every push to `main` or `master` branch will automatically:
1. Deploy agent to OpenClaw server
2. Update all Lambda functions

## Required Secrets

Add these secrets to your GitHub repo:

### 1. Go to Repo Settings
https://github.com/mtecfix/openclaw-automation/settings/secrets/actions

### 2. Add Secrets

Click "New repository secret" for each:

**SSH_PRIVATE_KEY**
```bash
# Get your SSH private key
cat ~/.ssh/metrotec2026.pem
# Copy entire output including -----BEGIN/END-----
```

**SERVER_IP**
```
100.56.11.242
```

**AWS_ACCESS_KEY_ID**
```bash
# Get from AWS credentials
cat ~/.aws/credentials | grep aws_access_key_id | head -1 | cut -d= -f2 | xargs
```

**AWS_SECRET_ACCESS_KEY**
```bash
# Get from AWS credentials
cat ~/.aws/credentials | grep aws_secret_access_key | head -1 | cut -d= -f2 | xargs
```

## Test Auto-Deploy

After adding secrets:

```bash
cd /mnt/c/Users/admin/openclaw-automation

# Make a small change
echo "# Test" >> README.md

# Commit and push
git add .
git commit -m "Test auto-deploy"
git push

# Watch deployment
# Go to: https://github.com/mtecfix/openclaw-automation/actions
```

## Manual Deploy

You can also trigger manually:
1. Go to: https://github.com/mtecfix/openclaw-automation/actions
2. Click "Deploy to OpenClaw"
3. Click "Run workflow"

## What Gets Deployed

**On every push:**
- ✅ Agent script → OpenClaw server
- ✅ Lambda functions → AWS

**Deployment time:** ~30 seconds

## Workflow File

Location: `.github/workflows/deploy.yml`

Edit to customize deployment behavior.

## Troubleshooting

**If deployment fails:**
1. Check secrets are set correctly
2. View logs in Actions tab
3. Verify SSH key has correct permissions
4. Ensure AWS credentials are valid

## Next Steps

1. Add secrets to GitHub
2. Push a change to test
3. Watch it auto-deploy!
