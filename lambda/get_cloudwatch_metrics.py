import json
import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    """Get CloudWatch metrics"""
    try:
        distribution_id = event.get('distributionId')
        days = event.get('days', 30)
        
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=days)
        
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/CloudFront',
            MetricName='Requests',
            Dimensions=[
                {'Name': 'DistributionId', 'Value': distribution_id},
                {'Name': 'Region', 'Value': 'Global'}
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=86400 * days,
            Statistics=['Sum']
        )
        
        total_requests = 0
        if response['Datapoints']:
            total_requests = response['Datapoints'][0]['Sum']
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'distributionId': distribution_id,
                'totalRequests': int(total_requests),
                'period': f'{days} days'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
