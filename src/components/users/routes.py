import os
from flask import Blueprint, jsonify
from src.library.helpers.response_builder import success_response

API_PREFIX = os.environ.get('API_PREFIX')
users = Blueprint("users", __name__, url_prefix=f'{API_PREFIX}/users')


@users.get('/')
async def index():
  return success_response('User routes connected', {'message': 'Hello, world!'})
