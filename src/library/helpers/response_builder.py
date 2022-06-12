def build_response(success: bool, message: str, data: dict = {}, error=None):
  response_body = {
      'success': success,
      'message': message,
  }

  if error:
    response_body['error'] = error
  else:
    response_body['data'] = data

  return (response_body)


def success_response(message, data):
  return build_response(success=True, message=message, data=data)


def error_response(message, error):
  return build_response(success=False, message=message, error=error)
