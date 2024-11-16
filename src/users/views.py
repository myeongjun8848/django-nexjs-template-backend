from ninja import NinjaAPI, Schema
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

@api.get('/hello')
def hello_world(request):
    return 'hello world'


class UserSchema(Schema):
    """
    사용자 스키마
    """
    id: int
    email: str

@api.get('/me', response=UserSchema, auth=JWTAuth())
def me(request):
    return request.user