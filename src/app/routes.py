from flask import Flask
from src.library.helpers.logger import logger
from src.components.auth.routes import auth
from src.components.users.routes import users


def register_routes(app: Flask):
  app.register_blueprint(auth)
  app.register_blueprint(users)
