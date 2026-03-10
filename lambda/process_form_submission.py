import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """Process form submission from S3"""
    try:
        bucket = event['bucket']
        key = event['key']
        
        # Get form data from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        form_data = json.loads(response['Body'].read())
        
        # Extract key fields
        extracted = {
            'clientName': form_data.get('name', ''),
            'email': form_data.get('email', ''),
            'phone': form_data.get('phone', ''),
            'caseType': form_data.get('caseType', ''),
            'description': form_data.get('description', ''),
            'submittedAt': form_data.get('timestamp', '')
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Form processed',
                'data': extracted
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
