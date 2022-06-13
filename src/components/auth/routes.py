import os
from flask import Blueprint
from src.library.helpers.response_builder import success_response
from src.library.helpers.raise_exception import raise_exception

API_PREFIX = os.environ.get('API_PREFIX')
auth = Blueprint("auth", __name__, url_prefix=f'{API_PREFIX}/auth')


@auth.get('/signup')
async def signup():
  try:
    return success_response('Auth routes connected', {'message': 'Hello, world!'})
  except Exception as error:
    raise_exception(error)
