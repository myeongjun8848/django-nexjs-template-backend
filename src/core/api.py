from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from helpers.error.handlers import register_exception_handlers

from posts.api import router as posts_router
from users.api import router as users_router

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

# 각 라우터를 고유한 prefix로 등록
api.add_router('/posts/', posts_router)
api.add_router('/users/', users_router)

register_exception_handlers(api)