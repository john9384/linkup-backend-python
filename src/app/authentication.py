from functools import wraps
from flask import request
from src.library.helpers.jwt_helper import decode_field
from werkzeug.exceptions import BadRequest, Unauthorized


def authentication_required(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = None
    if 'x-access-tokens' in request.headers:
      token = request.headers['x-access-tokens']
    if 'Authorization' in request.headers:
      authorization = request.headers['Authorization']
      auth_list = authorization.split(' ')
      token = auth_list[1]

    if not token:
      raise BadRequest("Token not supplied")
    try:
      jwt_payload = decode_field(token)
    except:
      raise Unauthorized("Unauthorized")

    return f(jwt_payload, *args, **kwargs)
  return decorator
