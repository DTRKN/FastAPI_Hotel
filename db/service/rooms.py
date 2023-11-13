from db.service.base import BaseService
from db.models.rooms import Rooms

class RoomService(BaseService):
    model = Rooms