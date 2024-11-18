from ninja.errors import ValidationError, AuthenticationError, Http404
from helpers.create_response import create_error_response
from .types import ErrorType

#
# error handlers
# 발생하는 에러를 캐치해 직접 핸들링한다.
def register_exception_handlers(api):

    # 일반 에러 핸들러 (구체적으로 명시하지 않은 에러는 이 핸들러를 통함. 마지막 방어선.)
    @api.exception_handler(Exception)
    def generic_errors(request, exc):
        error_response = create_error_response(ErrorType.INTERNAL, str(exc))
        return api.create_response(
            request,
            error_response,
            status=ErrorType.INTERNAL.value.status_code,
        )

    # django ninja 내장 ValidationError override
    @api.exception_handler(ValidationError)
    def validation_errors(request, exc):
        error_response = create_error_response(ErrorType.INVALID_ARGUMENT, str(exc))
        return api.create_response(
            request,
            error_response,
            status=ErrorType.INVALID_ARGUMENT.value.status_code,
        )

    # django ninja 내장 AuthenticationError 핸들러 override
    @api.exception_handler(AuthenticationError)
    def authentication_errors(request, exc):
        error_response = create_error_response(ErrorType.UNAUTHENTICATED, str(exc))
        return api.create_response(
            request,
            error_response,
            status=ErrorType.UNAUTHENTICATED.value.status_code,
        )

    # django ninja 내장 Http404 핸들러 override
    @api.exception_handler(Http404)
    def http404_errors(request, exc):
        error_response = create_error_response(ErrorType.NOT_FOUND, str(exc))
        return api.create_response(
            request,
            error_response,
            status=ErrorType.NOT_FOUND.value.status_code,
        )

    #
    # 커스텀 추가 에러 핸들러
    #

    # 권한 에러 핸들러
    @api.exception_handler(PermissionError)
    def permission_errors(request, exc):
        error_response = create_error_response(ErrorType.PERMISSION_DENIED, str(exc))
        return api.create_response(
            request,
            error_response,
            status=ErrorType.PERMISSION_DENIED.value.status_code,
        )
