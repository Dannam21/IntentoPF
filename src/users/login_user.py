import boto3
import jwt

SECRET_KEY = "your-secret-key"

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def handler(event, context):
    data = event['body']
    username = data['username']
    password = data['password']

    response = table.query(
        KeyConditionExpression="tenant_id = :tenant_id and username = :username",
        ExpressionAttributeValues={
            ':tenant_id': data['tenant_id'],
            ':username': username
        }
    )
    if response['Items'] and response['Items'][0]['password'] == password:
        token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
        return {'statusCode': 200, 'body': {'token': token}}
    else:
        return {'statusCode': 401, 'body': 'Invalid credentials'}
