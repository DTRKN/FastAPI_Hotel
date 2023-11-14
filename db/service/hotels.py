from db.service.base import BaseService
from db.service.bookings import BookingService
from db.models.hotels import Hotels
from db.database import async_session_maker
from sqlalchemy import select

class HotelService(BaseService):
    model = Hotels

    @classmethod
    async def find_all(cls, **filter):
        pass


