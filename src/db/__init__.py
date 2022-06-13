import os
from pathlib import Path

from flask_sqlalchemy import SQLAlchemy
import flask_migrate
from src.library.helpers.logger import logger

db = SQLAlchemy()
migrate = flask_migrate.Migrate()
migration_file_path = f'{Path(Path.cwd())}/src/db/migrations'
dev_env = os.environ.get('APP_ENV')


def setup_db(app) -> None:
  db.init_app(app)
  migrate.init_app(app, db, directory="src/db/migrations")
