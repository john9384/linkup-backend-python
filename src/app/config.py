from src.library.helpers.logger import logger
from src.config.dev import DevelopmentConfig
from src.config.prod import ProductionConfig
from src.config.test import TestConfig


def add_configurations(app, env='development'):
  if env == 'production':
    app.config.from_object(ProductionConfig)
  elif env == 'test':
    app.config.from_object(TestConfig)
  else:
    app.config.from_object(DevelopmentConfig)

  logger.info('Configurations loaded')
