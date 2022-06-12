from sqlalchemy.orm import Session
from .__init__ import db


class BaseRepository:
  def __init__(self, Model):
    self.Model = Model

  async def fetch_by_id(self, id):
    pass

  async def fetch_all(self):
    pass

  async def create(self, data: dict):
    pass

  async def update(self, id, data: dict):
    pass

  async def delete(self, id):
    pass
