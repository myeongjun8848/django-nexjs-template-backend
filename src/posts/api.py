from ninja import Router
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404
from .models import Post
from .schemas import PostIn, PostOut
from django.http import Http404

router = Router()


# get list
@router.get('/', response=list[PostOut], auth=JWTAuth())
def list_posts(request):
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
    
    return obj
   

# delete
@router.delete('/{post_id}', response={204: None})
def delete_post(request, post_id: int):
    try:
        obj = get_object_or_404(Post, id=post_id)
        obj.delete()
        return 204, None
    except Post.DoesNotExist:
        raise Http404("게시물을 찾을 수 없습니다")
    except Exception as e:
        raise Exception(f"삭제 중 오류가 발생했습니다: {str(e)}")
