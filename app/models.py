from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    password = Column(String)
    role = Column(String(6), nullable=True, default="user")

    products = relationship("Product", back_populates="owner")

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    image = Column(URLType)
    quantity = Column(Integer)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="products")
