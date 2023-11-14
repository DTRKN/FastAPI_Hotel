from db.service.base import BaseService
from db.models.rooms import Rooms
from db.models.bookings import Bookings
from sqlalchemy import select
from db.database import async_session_maker
from db.service.bookings import BookingService

class RoomService(BaseService):
    model = Bookings

    @classmethod
    async def find_all(cls, **filter):
        pass
