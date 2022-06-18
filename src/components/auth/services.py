
from http.client import BAD_REQUEST, CONFLICT
from src.library.helpers.jwt_helper import encode_field
from src.library.helpers.raise_exception import FormException, DatabaseExeption, ValidationException
from .form_validator import signup_validator, login_validator
from src.components.users.repository import user_repo
from src.library.utils.generate_field import generate_username
from src.library.utils.passlib_hash import encrypt_field, compare_field


async def signup_service(form_data: dict):
  form_errors = signup_validator(form_data)

  if len(form_errors) > 0:
    raise FormException(BAD_REQUEST, form_errors)

  del form_data['confirm_password']

  existing_user = await user_repo.fetch_by_email(form_data['email'])
  if existing_user:
    raise DatabaseExeption(
        CONFLICT,
        {
            'message': 'User with email already exist. Login instead',
            'email': form_data['email']
        }
    )

  form_data['username'] = generate_username(form_data['firstname'], form_data['lastname'])
  form_data['password'] = encrypt_field(form_data['password'])

  new_user = await user_repo.create(form_data)

  return {'email': new_user.email}


async def login_service(form_data: dict):
  form_errors = login_validator(form_data)
  if len(form_errors) > 0:
    raise FormException(form_errors)

  user = await user_repo.fetch_by_email(form_data['email'])

  if not user:
    raise DatabaseExeption(
        BAD_REQUEST,
        {
            'message': 'Invalid Credential',
            'email': form_data['email']
        })

  password_valid = compare_field(user.password, form_data['password'])

  if password_valid is False:
    raise DatabaseExeption(
        ValidationException,
        BAD_REQUEST,
        {
            'message': 'Invalid Credential',
            'email': form_data['email']
        })

  token = encode_field({'user_id': user.id})

  return {
      'email': user.email,
      'token': token
  }
