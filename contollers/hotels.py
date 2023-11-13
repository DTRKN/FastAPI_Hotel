from fastapi import APIRouter, HTTPException, status, Response, Depends
from db.service.bookings import BookingService
from db.service.hotels import HotelService
from db.service.rooms import RoomService

router = APIRouter(
    prefix='/hotels',
)
@router.get('/{location}')
async def get_hotels_city(
        location: str,
        date_from: str,
        date_to: str
):
    return await HotelService.find_all(location=location)

@router.get('/{id}/rooms')
async def get_hotels_rooms(
        id: int,
        date_from: str,
        date_to: str
):
    return await RoomService.find_all(hotel_id=id)



