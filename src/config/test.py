import os

from .base_config import BaseConfig


class TestConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DB_URI = 'sqlite:////test_database.db'
