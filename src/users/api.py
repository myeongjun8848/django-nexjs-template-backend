import random
from typing import Dict, Any

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from ninja import Router

from .schemas import RegisterIn, UserOut, VerifyEmailIn


router = Router()

# register
@router.post('/register', response={200: UserOut, 400: Dict[str, Any], 422: Dict[str, Any]})
def register(request, payload: RegisterIn):

    # 이미 존재하는 이메일인지 검증
    if get_user_model().objects.filter(email=payload.email).exists():
        return 409, {"detail": _("이미 존재하는 이메일입니다.")}

    # 비밀번호 검증
    try:
        validate_password(payload.password)
    except DjangoValidationError as e:
        return 400, {"detail": e.messages[0]}
        
    
    obj = get_user_model().objects.create_user(**payload.dict())
    
    # 이메일 인증 코드 생성
    verification_code = str(random.randint(100000, 999999))
    obj.verification_code = verification_code
    obj.save()

    # 이메일 인증 코드 전송
    send_mail(
        subject='이메일 인증 코드',
        message=f'인증 코드: {verification_code}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[obj.email],
    )

    return obj
    
        
@router.post('/verify-email', response={200: Dict[str, Any], 400: Dict[str, Any]})
def verify_email(request, payload: VerifyEmailIn):
    obj = get_user_model().objects.get(email=payload.email)
    if obj.verification_code != payload.verification_code:
        return 400, {"detail": _("인증 코드가 일치하지 않습니다.")}
    
    obj.email_verified = True
    obj.save()
    return 200, {"detail": _("이메일 인증이 완료되었습니다.")}