import os
from src.app import create_app

environment = os.environ.get('APP_ENV')

if __name__ == "__main__":
  app = create_app(environment)
  debug_mode = app.config['DEBUG'] | False
  app.run(host='localhost', port=5000, debug=debug_mode)
