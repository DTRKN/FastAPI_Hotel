from fastapi import APIRouter, HTTPException, status, Response, Depends
from db.service.bookings import BookingService
from db.service.hotels import HotelService
from db.service.rooms import RoomService
from datetime import date

router = APIRouter(
    prefix='/hotels',
    tags=['Hotel']
)
@router.get('/{location}')
async def get_hotels_city(
        location: str,
        date_from: date,
        date_to: date
):
    return await HotelService.find_all(location=location,
                                       date_from=date_from,
                                       date_to=date_to)

@router.get('/id/{hotel_id}')
async def get_hotels(
        hotel_id: int
):
    return True




