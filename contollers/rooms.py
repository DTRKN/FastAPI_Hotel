from fastapi import APIRouter, HTTPException, status, Response, Depends

router = APIRouter(
    prefix='/hotels',
)

@router.get('/id/{hotel_id}')
async def get_hotels(
        hotel_id: int
):
    return True