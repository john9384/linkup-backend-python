import os
from flask import Blueprint, request
from src.library.helpers.response_builder import success_response
from src.library.helpers.raise_exception import raise_exception
from .services import signup_service, login_service

API_PREFIX = os.environ.get('API_PREFIX')
auth = Blueprint("auth", __name__, url_prefix=f'{API_PREFIX}/auth')


@auth.post('/signup')
async def signup():
  try:
    form_data = request.json
    res_data = await signup_service(form_data)

    return success_response('Signup Complete', res_data)
  except Exception as error:
    print(error)
    raise_exception(error)


@auth.post('/login')
async def login():
  try:
    form_data = request.json
    res_data = await login_service(form_data)

    return success_response('Login Successful', res_data)
  except Exception as error:
    print(error)
    raise_exception(error)
