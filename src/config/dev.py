import os

from .base_config import BaseConfig


class DevelopmentConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
