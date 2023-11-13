from fastapi import Request, status, HTTPException, Depends
from jose import jwt, JWTError
from config import settings
from datetime import datetime
from db.service.user import UserService
from db.models.user import Users
from exceptions import (TokenExpireException,
                        UserIdNotFound,
                        UserException,
                        TokenAbsentException,
                        IncorrentTokenFormatException)

def get_token(request: Request):
    try:
        token = request.cookies.get('booking_access_token')
    except:
        raise TokenAbsentException

    return token
async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.KEY_JWT, settings.ALGO_JWT)
    except JWTError:
        raise IncorrentTokenFormatException

    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < int(datetime.utcnow().timestamp())):
        raise TokenExpireException

    user_id: int = int(payload.get('sub'))
    if not user_id:
        raise TokenExpireException

    user = await UserService.find_by_id(user_id)
    if user is None:
        raise UserIdNotFound
    return user

async def get_current_admin_user(admin: str, user: Users = Depends(get_current_user)):
    if admin == 'yes':
        return user
    else:
        raise UserException