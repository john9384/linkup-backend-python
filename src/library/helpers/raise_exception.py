from werkzeug.exceptions import InternalServerError, HTTPException


def raise_exception(error):
  if isinstance(error, HTTPException) is False:
    raise InternalServerError(str(error))

  raise error


class FormExceptions(HTTPException):
  def __init__(self, error_data: dict):
    self.code = 400
    self.description = 'Form validation error'
    self.data = error_data
  pass
