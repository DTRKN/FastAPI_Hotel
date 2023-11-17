from fastapi import APIRouter, HTTPException, status, Response, Depends
from db.service.rooms import RoomService
from datetime import date

router = APIRouter(
    prefix='/hotels',
    tags=['Rooms']
)

@router.get('/{id}/rooms')
async def get_hotels_rooms(
        id: int,
        date_from: date,
        date_to: date
):
    return await RoomService.find_all(room_id=id,
                                      date_from=date_from,
                                      date_to=date_to)