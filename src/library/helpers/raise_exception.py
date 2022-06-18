from werkzeug.exceptions import InternalServerError, HTTPException


def raise_exception(error):
  if isinstance(error, HTTPException) is False:
    raise InternalServerError(str(error))

  raise error


class FormException(HTTPException):
  def __init__(self, status_code, error_data: dict):
    self.code = status_code or 400
    self.description = 'Form validation error'
    self.data = error_data


class DatabaseExeption(HTTPException):
  def __init__(self, status_code, error_data: dict):
    self.code = status_code or 500
    self.description = 'Database error'
    self.data = error_data


class ValidationException(HTTPException):
  def __init__(self, status_code, error_data: dict):
    self.code = status_code or 500
    self.description = 'Database error'
    self.data = error_data
