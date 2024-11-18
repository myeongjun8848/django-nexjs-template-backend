from django.http import Http404
from django.shortcuts import get_object_or_404

from ninja import Router
from ninja_jwt.authentication import JWTAuth

from .models import Post
from .schemas import PostIn, PostOut
from schemas.response import SuccessResponse, ErrorResponse

from helpers.create_response import create_success_response

router = Router(tags=["posts"])

# get list
@router.get('/', response=SuccessResponse[list[PostOut]] | ErrorResponse)
def list_posts(request):
    qs = Post.objects.all()
    return create_success_response(qs)

# create
@router.post('/', response=SuccessResponse[PostOut] | ErrorResponse)
def create_post(request, payload: PostIn):
    obj = Post.objects.create(**payload.dict())
    return create_success_response(obj)

# get one
@router.get('/{post_id}', response=SuccessResponse[PostOut] | ErrorResponse)
def get_post(request, post_id: int):
    obj = get_object_or_404(Post, id=post_id)
    return create_success_response(obj) 

# update
@router.put('/{post_id}', response=SuccessResponse[PostOut] | ErrorResponse)
def update_post(request, post_id: int, payload: PostIn):
    obj = get_object_or_404(Post, id=post_id)
    
    payload_dict = payload.dict()
    for key, value in payload_dict.items():
        setattr(obj, key, value)
    obj.save()
    
    return create_success_response(obj)
   

# delete
@router.delete('/{post_id}', response=SuccessResponse[None] | ErrorResponse)
def delete_post(request, post_id: int):
    try:
        obj = get_object_or_404(Post, id=post_id)
        obj.delete()
        return create_success_response(None)
    except Post.DoesNotExist:
        raise Http404("게시물을 찾을 수 없습니다")
    except Exception as e:
        raise Exception(f"삭제 중 오류가 발생했습니다: {str(e)}")
