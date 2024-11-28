import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def handler(event, context):
    data = event['body']
    user_id = str(uuid.uuid4())
    user = {
        'tenant_id': data['tenant_id'],  # Clave de partición
        'user_id': user_id,              # Clave de ordenamiento
        'username': data['username'],
        'email': data['email'],
        'password': data['password']    # En producción, hashear la contraseña
    }
    table.put_item(Item=user)
    return {
        'statusCode': 201,
        'body': f"User {user_id} created successfully!"
    }
