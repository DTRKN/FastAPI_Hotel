from db.service.base import BaseService
from db.models.user import Users

class UserService(BaseService):
    model = Users

