from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    password = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
