import os
import jwt
import datetime

SECRET_KEY = os.environ.get('DATABASE_URI')
ALGORITHM = os.environ.get('JWT_ALGORITHM') or "HS256"


def encode_field(payload: dict):
  payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
  return jwt.encode(payload, SECRET_KEY, ALGORITHM)


def decode_field(token):
  return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
