from pydantic import BaseModel
from datetime import date


class SchemaBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        orm_mode = True

class BookingData(BaseModel):
    Bookings: SchemaBooking