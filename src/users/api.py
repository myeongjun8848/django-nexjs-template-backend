import random
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.template.loader import render_to_string

from ninja.errors import ValidationError, Http404
from ninja import Router

from helpers.create_response import create_success_response
from schemas.response import SuccessResponse, ErrorResponse
from .schemas import RegisterIn, UserOut, VerifyEmailIn


router = Router(tags=["users"])

# register
@router.post('/register', response={200: SuccessResponse[UserOut], 400: ErrorResponse, 422: ErrorResponse})
def register(request, payload: RegisterIn):

    # 이미 존재하는 이메일인지 검증
    if get_user_model().objects.filter(email=payload.email).exists():
        raise ValidationError("Email already exists.")

    # 비밀번호 검증
    try:
        validate_password(payload.password)
    except DjangoValidationError as e: # validate_password는 django 내장 예외를 발생시키므로 이를 처리하기 위해 DjangoValidationError 사용
        raise ValidationError(_(e.messages[0]))
        
    
    with transaction.atomic(): # 이메일 전송 실패 시 롤백 기능 (생성한 사용자 삭제)
        obj = get_user_model().objects.create_user(**payload.dict())
        
        # 이메일 인증 코드 생성
        verification_code = str(random.randint(100000, 999999))
        obj.verification_code = verification_code
        obj.save()

        try:
            # 이메일 템플릿 렌더링
            email_content = render_to_string('users/verification_email.html', {
                'verification_code': verification_code
            })
            
            send_mail(
                subject=(_("이메일 인증 코드")),
                message=email_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[obj.email],
                fail_silently=False,
                html_message=email_content,
            )

            return create_success_response(obj)
        except (SMTPException, Exception) as e:
            raise Exception(_("알 수 없는 오류가 발생했습니다. 잠시 후 다시 시도해주세요."))
    
        
@router.post('/verify-email', response={200: SuccessResponse[dict], 400: ErrorResponse, 404: ErrorResponse})
def verify_email(request, payload: VerifyEmailIn):
    try:
        obj = get_user_model().objects.get(email=payload.email)
    except get_user_model().DoesNotExist:
        raise Http404("User not found")

    if obj.verification_code != payload.verification_code:
        raise ValidationError(_("인증 코드가 일치하지 않습니다."))
    
    obj.email_verified = True
    obj.save()
    return create_success_response(_("이메일 인증이 완료되었습니다."))
