import os
from flask import Blueprint
from src.library.helpers.response_builder import success_response
from src.library.helpers.raise_exception import raise_exception
from .services import signup

API_PREFIX = os.environ.get('API_PREFIX')
auth = Blueprint("auth", __name__, url_prefix=f'{API_PREFIX}/auth')


@auth.get('/signup')
async def signup():
  try:
    res_data = await signup()
    return success_response('Signup Complete', res_data)
  except Exception as error:
    raise_exception(error)
