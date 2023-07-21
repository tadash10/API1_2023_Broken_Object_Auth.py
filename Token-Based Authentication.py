# api.py
import jwt
import datetime

SECRET_KEY = 'your_secret_key'

def generate_token(user):
    payload = {
        'user_id': user.user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        raise RuntimeError("Token has expired.")
    except jwt.InvalidTokenError:
        raise RuntimeError("Invalid token.")

def api_function_get_object(auth_token, obj_id):
    try:
        # Token-Based Authentication
        user_id = decode_token(auth_token)
        authenticated_user = User(user_id=user_id)

        # Input Validation (rest of the code remains the same)
