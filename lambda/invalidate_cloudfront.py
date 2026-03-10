import json
import boto3
import time

cloudfront = boto3.client('cloudfront')

def lambda_handler(event, context):
    """Invalidate CloudFront cache"""
    try:
        distribution_id = event['distributionId']
        paths = event.get('paths', ['/*'])
        
        response = cloudfront.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': len(paths),
                    'Items': paths
                },
                'CallerReference': f'lambda-{int(time.time())}'
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Invalidation created',
                'invalidationId': response['Invalidation']['Id'],
                'status': response['Invalidation']['Status']
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
