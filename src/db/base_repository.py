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
    entity = self.Model(**data)
    db.session.add(entity)
    db.session.commit()
    db.session.refresh(entity)

    return entity

  async def update(self, id, data: dict):
    pass

  async def delete(self, id):
    pass
