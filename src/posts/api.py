from ninja import Router
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from .models import Post
from .schemas import PostIn, PostOut

router = Router()

# get list
@router.get('/', response=list[PostOut], auth=JWTAuth())
def list_posts(request):
    print("is_authenticated @@@@@@@@@@@@", request.user.is_authenticated)
    qs = Post.objects.all()
    return qs

# create
@router.post('/', response=PostOut)
def create_post(request, payload: PostIn):
    obj = Post.objects.create(**payload.dict())
    return obj

# get one
@router.get('/{post_id}', response=PostOut)
def get_post(request, post_id: int):
    obj = get_object_or_404(Post, id=post_id)
    return obj

# update
@router.put('/{post_id}', response=PostOut)
def update_post(request, post_id: int, payload: PostIn):
    obj = get_object_or_404(Post, id=post_id)
    obj.title = payload.title
    obj.content = payload.content
    obj.save()
   

# delete
@router.delete('/{post_id}')
def delete_post(request, post_id: int):
    obj = get_object_or_404(Post, id=post_id)
    obj.delete()
    return {"success": True}