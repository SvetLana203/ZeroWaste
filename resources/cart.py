from models.db import db
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload
from models.cart import Cart
from models.user import User

class Carts(Resource):
  def get(self):
    carts = Cart.find_all()
    return carts

  def post(self):
    data = request.get_json()
    params = {}
    for k in data.keys():
      params[k] = data[k]
    cart = Cart(**params)
    cart.create()
    return cart.json(), 201

class CartInfo(Resource):
  def get(self, user_id):
    cart = Cart.query.options(joinedload("user")).filter_by(user_id=user_id).first()
    return {**cart.json(), "cart": cart.user.json()}


