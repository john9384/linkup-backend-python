import os

from .base_config import BaseConfig


class TestConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:////test_database.db'
