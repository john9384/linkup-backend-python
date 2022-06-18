import datetime
import uuid


def generate_username(firstname, lastname):
  """
  Generate a username from the first and last name.
  """
  ts = str(datetime.datetime.now().timestamp())
  start = len(ts) - 4
  ts_splice = ts[start: len(ts)]
  f_slice = firstname[0:3]
  l_slice = lastname[0:2]

  return f'{f_slice}{l_slice}{ts_splice}'.lower()


def generate_id() -> str:
  """
  Generate random id.
  """
  uuid_str = str(uuid.uuid4())
  uuid_list = uuid_str.split('-')
  ts = str(datetime.datetime.now().timestamp())
  start = len(ts) - 4
  ts_splice = ts[start: len(ts)]
  id = str(ts_splice).join(uuid_list)
  return str(id)
