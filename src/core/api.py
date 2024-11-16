from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController


api = NinjaExtraAPI()

# auth
api.register_controllers(NinjaJWTDefaultController)
# users
api.add_router('users/', "users.api.router")

# posts
api.add_router('posts/', "posts.api.router")


