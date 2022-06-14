from src.library.helpers.validator_class import Validator
from src.library.utils.list_methods import filter_list_none, list_diff

validator = Validator()


def signup_validator(form: dict):
  required_fields = ['firstname', 'lastname', 'email', 'password', 'confirm_password']
  error_list = []

  null_fields = list_diff(required_fields, list(form.keys()))

  if null_fields:
    for field in null_fields:
      error_list.append({field: f'{field} is required'})
  else:
    for key in form.items():
      if key[0] == 'firstname':
        error_list.append(validator.validate_text(key[0], key[1]))
      if key[0] == 'lastname':
        error_list.append(validator.validate_text(key[0], key[1]))
      if key[0] == 'email':
        error_list.append(validator.validate_email(key[1]))
      if key[0] == 'password':
        error_list.append(validator.validate_text(key[0], key[1]))
      if key[0] == 'confirm_password' and key[1] != form['password']:
        error_list.append({'confirm_password': 'Password does not match'})

  return filter_list_none(error_list)


def login_validator(form: dict):
  required_fields = ['email', 'password']
  error_list = []

  null_fields = list_diff(required_fields, list(form.keys()))

  if null_fields:
    for field in null_fields:
      error_list.append({field: f'{field} is required'})
  else:
    for key in form.items():
      if key[0] == 'email':
        error_list.append(validator.validate_email(key[1]))
      if key[0] == 'password':
        error_list.append(validator.validate_text(key[0], key[1]))

  return filter_list_none(error_list)
