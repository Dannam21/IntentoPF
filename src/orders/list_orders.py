import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def handler(event, context):
    tenant_id = event['queryStringParameters']['tenant_id']

    response = table.query(
        KeyConditionExpression="tenant_id = :tenant_id",
        ExpressionAttributeValues={':tenant_id': tenant_id}
    )
    return {
        'statusCode': 200,
        'body': response['Items']
    }
