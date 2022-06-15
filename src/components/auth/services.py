
from src.library.helpers.raise_exception import FormExceptions
from .form_validator import signup_validator, login_validator
from src.components.users.repository import user_repo
from src.library.utils.generate_username import generate_username
from src.library.utils.passlib_hash import encrypt_field


async def signup_service(form_data: dict):
  form_errors = signup_validator(form_data)

  if len(form_errors) > 0:
    raise FormExceptions(form_errors)

  del form_data['confirm_password']

  form_data['username'] = generate_username(form_data['firstname'], form_data['lastname'])
  form_data['password'] = encrypt_field(form_data['password'])

  new_user = await user_repo.create(form_data)

  return {
      'message': 'Signup Complete',
      'data': {'email': new_user.email}
  }


async def login_service(form_data: dict):
  # Validate the form data
  # check if user with email exists
  # fetch the user if the user exists
  # compare the password with the one in db
  # generate token to be use

  ### TODO: Implement route protection ###
  # TODO: complete login service
  # TODO: complete token generation
  # TODO: Custum form for validation
  return {
      'message': 'Login Complete',
      'data': {'email': 'test@test.com', 'token': 'test'}
  }
