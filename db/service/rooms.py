from db.service.base import BaseService
from db.models.rooms import Rooms
from db.models.bookings import Bookings
from sqlalchemy import select
from db.database import async_session_maker
from db.service.bookings import BookingService

class RoomService(BaseService):
    model = Rooms

    @classmethod
    async def find_all(cls, **filter):
        rooms_left = await BookingService.get_rooms_left(room_id=filter['room_id'],
                                                         date_to=filter['date_to'],
                                                         date_from=filter['date_from'])
        data = await BaseService.find_all(**filter)

        return data, rooms_left

