import os
from flask import Blueprint, jsonify
from src.app.authentication import authentication_required
from src.library.helpers.response_builder import success_response
from .model import User

API_PREFIX = os.environ.get('API_PREFIX')
users = Blueprint("users", __name__, url_prefix=f'{API_PREFIX}/users')


@users.get('/')
@authentication_required
def index(jwt_payload):
  return success_response('User routes connected', jwt_payload)
