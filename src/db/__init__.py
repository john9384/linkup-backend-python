import os
from pathlib import Path

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, init as migration_init
from src.library.helpers.logger import logger

db = SQLAlchemy()
migrate = Migrate()
migration_file_path = f'{Path(Path.cwd())}/src/db/migrations'


def setup_db(app) -> None:
  db.init_app(app)
  migrate.init_app(app, db, directory="src/db/migrations")

  if os.path.exists(migration_file_path) is False:
    migration_init(directory='src/db/migrations')
    logger.info('Migrations initialized')
