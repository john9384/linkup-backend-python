import os
from flask import Blueprint, jsonify
from src.library.helpers.response_builder import success_response

API_PREFIX = os.environ.get('API_PREFIX')

auth = Blueprint("auth", __name__, url_prefix=f'{API_PREFIX}/auth')


@auth.get('/')
async def index():
  return success_response('Auth routes connected', {'message': 'Hello, world!'})
