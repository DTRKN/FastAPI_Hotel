from db.database import Base
from sqlalchemy import Column, Integer, String


class Users(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
