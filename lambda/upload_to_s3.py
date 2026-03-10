import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """Upload content to S3 bucket"""
    try:
        bucket = event['bucket']
        key = event['key']
        content = event['content']
        content_type = event.get('contentType', 'text/html')
        
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=content,
            ContentType=content_type
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Uploaded {key} to {bucket}',
                'url': f's3://{bucket}/{key}'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
