import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def handler(event, context):
    data = event['body']
    order_id = str(uuid.uuid4())
    order = {
        'tenant_id': data['tenant_id'],  # Clave de partición
        'order_id': order_id,           # Clave de ordenamiento
        'products': data['products'],
        'total_price': data['total_price'],
        'status': 'Pending'
    }
    table.put_item(Item=order)
    return {
        'statusCode': 201,
        'body': f"Order {order_id} created successfully!"
    }
