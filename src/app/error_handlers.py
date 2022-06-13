from flask import json
from werkzeug.exceptions import HTTPException
from src.library.helpers.response_builder import error_response


def configure_error_handlers(app):

  @app.errorhandler(HTTPException)
  def handle_exception(e):
    error_data = {
        "status_code": e.code,
        "name": e.name,
        "description": e.description,
    }

    return error_response(e.description, error_data)
