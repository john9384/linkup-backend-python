import os


class BaseConfig():
  """
  Base configuration class
  """
  DEBUG = False
  TESTING = False
  SECRET_KEY = os.environ.get("SECRET_KEY")
  SQLALCHEMY_DATABASE_URI = 'sqlite:////default.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
