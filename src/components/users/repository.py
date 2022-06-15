from src.db.base_repository import BaseRepository
from .model import User


class UserRepository(BaseRepository):
  pass


user_repo = UserRepository(User)
