import os
import logging

from pathlib import Path


class CustomFormatter(logging.Formatter):

  green = "\x1b[32;20m"
  grey = "\x1b[38;20m"
  yellow = "\x1b[33;20m"
  red = "\x1b[31;20m"
  bold_red = "\x1b[31;1m"
  reset = "\x1b[0m"
  format = "%(asctime)s - [%(levelname)s] - %(message)s (%(filename)s:%(lineno)d)"

  FORMATS = {
      logging.DEBUG: grey + format + reset,
      logging.INFO: green + format + reset,
      logging.WARNING: yellow + format + reset,
      logging.ERROR: red + format + reset,
      logging.CRITICAL: bold_red + format + reset
  }

  def format(self, record):
    log_fmt = self.FORMATS.get(record.levelno)
    formatter = logging.Formatter(log_fmt)
    return formatter.format(record)


class Logger:
  log_file_path = f'{Path(Path.cwd())}/src/logs'

  def __init__(self) -> None:
    self.create_log_files()
    self.info = self.config_info()
    self.debug = self.config_debug()
    self.warning = self.config_warning()
    self.error = self.config_error()
    self.critical = self.config_critical()

  def create_log_files(self):
    if os.path.exists(self.log_file_path):
      return
    os.makedirs(self.log_file_path)

  def config_info(self):
    logger = logging.getLogger('info')
    logger.setLevel(logging.INFO)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(CustomFormatter())
    fileHandler = logging.FileHandler(f'{self.log_file_path}/info.log')
    fileHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(CustomFormatter())
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    return logger.info

  def config_debug(self):
    logger = logging.getLogger('debug')
    logger.setLevel(logging.DEBUG)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(CustomFormatter())
    fileHandler = logging.FileHandler(f'{self.log_file_path}/debug.log')
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(CustomFormatter())
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    return logger.debug

  def config_warning(self):
    logger = logging.getLogger('warning')
    logger.setLevel(logging.WARNING)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.WARNING)
    consoleHandler.setFormatter(CustomFormatter())
    fileHandler = logging.FileHandler(f'{self.log_file_path}/warning.log')
    fileHandler.setLevel(logging.WARNING)
    fileHandler.setFormatter(CustomFormatter())
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    return logger.warning

  def config_error(self):
    logger = logging.getLogger('error')
    logger.setLevel(logging.ERROR)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.ERROR)
    consoleHandler.setFormatter(CustomFormatter())
    fileHandler = logging.FileHandler(f'{self.log_file_path}/error.log')
    fileHandler.setLevel(logging.ERROR)
    fileHandler.setFormatter(CustomFormatter())
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    return logger.error

  def config_critical(self):
    logger = logging.getLogger('critical')
    logger.setLevel(logging.CRITICAL)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.CRITICAL)
    consoleHandler.setFormatter(CustomFormatter())
    fileHandler = logging.FileHandler(f'{self.log_file_path}/critical.log')
    fileHandler.setLevel(logging.CRITICAL)
    fileHandler.setFormatter(CustomFormatter())
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)
    return logger.critical


logger = Logger()
