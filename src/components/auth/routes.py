import os
from flask import Blueprint, request
from http.client import CREATED, OK
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

    return success_response(
        status_code=CREATED,
        message='Signup Complete',
        data=res_data
    )
  except Exception as error:
    raise_exception(error)


@auth.post('/login')
async def login():
  try:
    form_data = request.json
    res_data = await login_service(form_data)

    return success_response(
        status_code=OK,
        message='Login Successful',
        data=res_data
    )
  except Exception as error:
    raise_exception(error)
