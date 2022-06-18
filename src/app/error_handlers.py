from flask import json
from werkzeug.exceptions import HTTPException
from src.library.helpers.response_builder import error_response


def configure_error_handlers(app):

  @app.errorhandler(HTTPException)
  def handle_exception(e):
    error_data = {}
    if hasattr(e, 'data'):
      error_data = e.data

    return error_response(
        status_code=e.code,
        message=e.description,
        error=error_data
    )
