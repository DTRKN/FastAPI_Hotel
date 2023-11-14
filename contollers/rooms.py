from fastapi import APIRouter, HTTPException, status, Response, Depends
from db.service.rooms import RoomService

router = APIRouter(
    prefix='/hotels',
    tags=['Rooms']
)

@router.get('/{id}/rooms')
async def get_hotels_rooms(
        id: int,
        date_from: str,
        date_to: str
):
    return await RoomService.find_all(hotel_id=id,
                                      date_from=date_from,
                                      date_to=date_to)