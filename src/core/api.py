from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from errors.handlers import register_exception_handlers


api = NinjaExtraAPI()

# auth
api.register_controllers(NinjaJWTDefaultController)
# users
api.add_router('users/', "users.api.router")

# posts
api.add_router('posts/', "posts.api.router")

# 에러 핸들러 등록
register_exception_handlers(api)