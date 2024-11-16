import re
from pydantic import field_validator
from django.utils.translation import gettext_lazy as _
from ninja.errors import ValidationError
from ninja import Schema

class RegisterIn(Schema):
    email: str
    password: str

    @field_validator('email')
    def validate_email(cls, v):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', v):
            raise ValidationError(_('이메일 형식이 올바르지 않습니다.'))
        return v


class UserOut(Schema):
    id: int
    email: str


class VerifyEmailIn(Schema):
    email: str
    verification_code: str

    @field_validator('verification_code')
    def validate_verification_code(cls, v):
        if not re.match(r'^\d{6}$', v):
            raise ValidationError(_('인증 코드는 6자리 숫자여야 합니다.'))
        return v
