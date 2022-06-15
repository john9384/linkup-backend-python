import uuid
from src.db import db
from datetime import datetime


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.String, primary_key=True, default=str(uuid.uuid1()))
  firstname = db.Column(db.String, nullable=False)
  lastname = db.Column(db.String,  nullable=False)
  email = db.Column(db.String, unique=True,  nullable=False)
  password = db.Column(db.String,  nullable=False)
  email_veirified = db.Column(db.Boolean, default=False)
  phone = db.Column(db.String)
  dob = db.Column(db.DateTime)
  gender = db.Column(db.String)
  religion = db.Column(db.String)
  username = db.Column(db.String, unique=True, nullable=False)
  avatar = db.Column(db.String)
  bg_url = db.Column(db.String)
  created_at = db.Column(db.DateTime, default=datetime.now())
  updated_at = db.Column(db.DateTime, default=datetime.now())

  def __repr__(self) -> str:
    return f'User >>> {self.email}'
