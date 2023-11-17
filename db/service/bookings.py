from db.models.bookings import Bookings
from db.models.rooms import Rooms
from db.service.base import BaseService
from sqlalchemy import select, and_, or_, func, insert, delete
from datetime import date
from db.database import engine, async_session_maker
from exceptions import RoomCannotBeBooked, BookingsIdNotFound

class BookingService(BaseService):
    model = Bookings
    """
    WITH booked_rooms AS (
        SELECT * FROM bookings
        WHERE room_id = 1 AND
        (date_from >= '2022-01-05' AND date_from <= '2022-10-10') OR
        (date_from <= '2022-01-05' AND date_to > '2022-01-05')
        )
    
    SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
    LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
    WHERE rooms.id = 1
    GROUP BY rooms.quantity, booked_rooms.room_id
    ;"""
    @classmethod
    async def get_rooms_left(cls,
                             room_id: int,
                             date_from: date,
                             date_to: date,
                             ):

        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == room_id,
                    or_(
                        and_(Bookings.date_from >= date_from,
                             Bookings.date_from <= date_to)
                        ,
                        and_(Bookings.date_from <= date_from,
                             Bookings.date_to > date_from)
                    )
                )
            ).cte("booked_rooms")

            get_rooms_left = select(Rooms.quantity - func.count(booked_rooms.c.room_id).label('rooms_left')
                                    ).select_from(Rooms).join(
                booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
            ).where(Rooms.id == room_id).group_by(
                Rooms.quantity, booked_rooms.c.room_id
            )
            print('------------')
            print(get_rooms_left.compile(engine, compile_kwargs={"literal_binds": True}))
            print('------------')

            rooms_left = await session.execute(get_rooms_left)
            rooms_left: int = rooms_left.scalar()
            return int(rooms_left)
    @classmethod
    async def add(
            cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date,
                  ):
        async with async_session_maker() as session:
            rooms_left = await cls.get_rooms_left(room_id,
                                            date_from,
                                            date_to)

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_booking = insert(Bookings).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price,
                ).returning(Bookings)

                new_booking = await session.execute(add_booking)
                await session.commit()
                return [new_booking.scalar(), rooms_left]

            else:
                return None
    @classmethod
    async def delete_id_booking(
                     cls,
                     booking_id: int):
        async with async_session_maker() as session:
            result = BaseService.find_one_or_none(id=booking_id)
            if not result:
                query = delete(cls.model).filter_by(id=booking_id)
                await session.execute(query)
                await session.commit()
                return f'Del booking_id: {booking_id}'
            else:
                raise BookingsIdNotFound