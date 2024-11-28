import jwt
import os

SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'mysecretkey')

def validate_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido
