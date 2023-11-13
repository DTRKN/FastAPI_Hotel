from fastapi import APIRouter, HTTPException, status, Response, Depends
from schemas.user import SUserAuth
from db.service.user import UserService
from auth.auth import get_password_hash, authenticate_user, create_access_token
from db.models.user import Users
from depends.token_user import get_current_user, get_current_admin_user
from exceptions import UserAlreadyExistsException, UserWrongEmailOrPasswordException

router = APIRouter(
    prefix='/auth',
    tags=[' Пользователь'],
)

@router.get('/get')
async def get():
    result = await UserService.find_all()
    return result


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UserService.find_one_or_none(email=user_data.User.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.User.password)
    await UserService.update(email=user_data.User.email, hash_password=hashed_password)
    return hashed_password

@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.User.email, user_data.User.password)
    if not user:
        raise UserWrongEmailOrPasswordException
    access_token = create_access_token({'sub': str(user.Users.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True, secure=True)
    return access_token

@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")

@router.get('/me')
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user

@router.get('/me_admin')
async def admin_view_users(current_user: Users = Depends(get_current_admin_user)):
    res = await UserService.find_all()
    return res



