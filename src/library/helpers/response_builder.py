from flask import Response
from http.client import INTERNAL_SERVER_ERROR, OK
import json


def build_response(status_code: int, success: bool, message: str, data: dict = {}, error=None):
  response_body = {
      'success': success,
      'message': message
  }

  if error:
    response_body['data'] = error
  else:
    response_body['data'] = data

  return Response(json.dumps(response_body), status=status_code, mimetype="application/json")


def success_response(message, data, status_code: int = OK):
  return build_response(success=True, message=message, data=data, status_code=status_code)


def error_response(message, error, status_code: int = INTERNAL_SERVER_ERROR):
  return build_response(success=False, message=message, error=error, status_code=status_code)
