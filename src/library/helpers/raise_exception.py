from werkzeug.exceptions import InternalServerError, HTTPException


def raise_exception(error):
  if isinstance(error, HTTPException) is False:
    raise InternalServerError(str(error))

  raise error
