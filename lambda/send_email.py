import json
import boto3

ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event, context):
    """Send email via SES"""
    try:
        to_email = event['to']
        subject = event['subject']
        body = event['body']
        from_email = event.get('from', 'mrtechfixes.ai@gmail.com')
        
        response = ses.send_email(
            Source=from_email,
            Destination={'ToAddresses': [to_email]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}}
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Email sent',
                'messageId': response['MessageId']
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
