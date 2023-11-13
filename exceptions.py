from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = 404
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'The user already exist'

class UserWrongEmailOrPasswordException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'The user wrong password or email'

class UserIdNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'The user id not found'

class TokenExpireException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token expired'

class TokenAbsentException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token None'

class IncorrentTokenFormatException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'The wrong token format'

class UserException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED

class RoomCannotBeBooked(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'There are no rooms available'

