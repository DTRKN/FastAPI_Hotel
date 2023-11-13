from fastapi import APIRouter, Request, Depends
from db.service.bookings import BookingService
from depends.token_user import get_current_user, get_token
from db.models.user import Users
from datetime import date
from exceptions import RoomCannotBeBooked

router = APIRouter(
    prefix='/bookings',
    tags=['бронирование'],
)

@router.post("/booking_room")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user)
):
    bookings = await BookingService.add(user.Users.id, room_id, date_from, date_to)
    if bookings is None:
        raise RoomCannotBeBooked
    return f'Cost: {bookings[0].total_cost}, left: {bookings[1] - 1}'

@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingService.find_all(user_id=user.User.id)

@router.delete('/{booking_id}')
async def found_bookings(booking_id):
    return None

