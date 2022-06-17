from src.db.base_repository import BaseRepository
from .model import User


class UserRepository(BaseRepository):
  async def fetch_by_email(self, email: str):
    entity = self.Model.query.filter_by(email=email).first()
    return entity


user_repo = UserRepository(User)
