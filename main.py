from fastapi import FastAPI
from contollers.bookings import router as router_booking
from contollers.user import router as router_user
from contollers.rooms import router as router_rooms
from contollers.hotels import router as router_hotels

app = FastAPI()
app.include_router(router_user)
app.include_router(router_booking)
app.include_router(router_rooms)
app.include_router(router_hotels)

