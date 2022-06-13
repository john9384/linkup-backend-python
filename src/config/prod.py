import os
from .base_config import BaseConfig


class ProductionConfig(BaseConfig):
  DEBUG = False
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
