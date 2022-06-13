from flask import Flask
from src.db import setup_db
from .config import add_configurations
from .routes import register_routes
from .error_handlers import configure_error_handlers


def create_app(env="development") -> Flask:
  app = Flask(__name__, instance_relative_config=True)
  # Setting configurations for the app
  add_configurations(app, env)

  # Adding the database to the app
  with app.app_context():
    setup_db(app)

  @app.get("/")
  def index():
    return {"message": "LinkUp api is running"}

  # Registering the routes for the app
  register_routes(app)

  # Configure Error handlers
  configure_error_handlers(app)

  return app
