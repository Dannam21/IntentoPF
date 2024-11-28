import boto3
from botocore.exceptions import ClientError

# Configuración de cliente DynamoDB
def get_dynamo_client():
    return boto3.client('dynamodb', region_name='us-east-1')

# Cliente DocumentClient (más usado para operaciones como PutItem, Query)
def get_dynamo_document_client():
    return boto3.client('dynamodb', region_name='us-east-1')

# Función para hacer un PutItem (ejemplo)
def put_item(table_name, item):
    client = get_dynamo_document_client()
    try:
        response = client.put_item(
            TableName=table_name,
            Item=item
        )
        return response
    except ClientError as e:
        print(f"Error al insertar item: {e}")
        return None
