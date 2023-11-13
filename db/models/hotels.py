from db.database import Base
from sqlalchemy import Column, Integer, String, JSON

class Hotels(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)
    services = Column(JSON, nullable=False)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)