from datetime import datetime
from models.db import db

class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False, unique=True)
  created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())
  items = db.relationship("Item", cascade='all', backref=db.backref('items', lazy=True))

  def __init__(self, name, email):
    self.name = name
    self.email = email

  def json(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "created_at": str(self.created_at),
      "updated_at": str(self.updated_at)
    }

  def create(self):
    db.session.add(self)
    db.session.commit()
    return self

  @classmethod
  def find_all(cls):
    return User.query.all()

  @classmethod 
  def find_by_id(cls, user_id):
    return User.query.filter_by(id=user_id).first()

  @classmethod
  def find_by_email(cls, user_id):
    user = User.query.filter_by(email=user_id).first()
    return user