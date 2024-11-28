import jwt

SECRET_KEY = "your-secret-key"

def handler(event, context):
    token = event['headers'].get('Authorization')
    if not token:
        return {'statusCode': 403, 'body': 'Token required'}

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return {'statusCode': 200, 'body': decoded}
    except jwt.ExpiredSignatureError:
        return {'statusCode': 401, 'body': 'Token expired'}
    except jwt.InvalidTokenError:
        return {'statusCode': 401, 'body': 'Invalid token'}
