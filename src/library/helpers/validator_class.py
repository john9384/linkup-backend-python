from csv import list_dialects
import re
from werkzeug.exceptions import BadRequest


class Validator():
  def __init__(self):
    pass

  def validate_email(self, email):
    # TODO: Fix regex wrong match
    reg = re.compile("^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+.(?:\.[a-zA-Z0-9-]+)*$")
    if not email or email == '':
      return {'email': 'Email is required'}
    elif re.match(reg, email):
      return {'email': 'Email is not valid'}

  def validate_text(self, field, text):
    reg = re.compile("^[a-zA-z ,.'-]+$")
    print(text, field)
    if not text or text == '':
      return {field: f'{field} is required'}
    elif not re.match(reg, text):
      return {field: f'{field.title()} must be alphabetic'}
