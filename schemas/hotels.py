from pydantic import BaseModel
from datetime import date


class SchemaHotels(BaseModel):
    location: str
    date_from: date
    date_to: date

    class Config:
        orm_mode = True

class HotelsData(BaseModel):
    Hotels: SchemaHotels