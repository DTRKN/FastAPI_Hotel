from pydantic import BaseModel
from datetime import date


class SchemaRoom(BaseModel):
    rooms_id: int
    date_from: date
    date_to: date

    class Config:
        orm_mode = True

class RoomData(BaseModel):
    Rooms: SchemaRoom