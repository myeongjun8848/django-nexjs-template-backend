from ninja.errors import ValidationError, AuthenticationError, Http404
from errors.types import ErrorType

#
# error handlers
#
def register_exception_handlers(api):

    # 일반 에러 핸들러 (구체적으로 명시하지 않은 에러는 이 핸들러를 통함. 마지막 방어선.)
    @api.exception_handler(Exception)
    def generic_errors(request, exc):
        error_response = ErrorType.INTERNAL.create_error_response(str(exc))
        return api.create_response(
            request,
            error_response,
            status=500,
        )

    # django ninja 내장 ValidationError override
    @api.exception_handler(ValidationError)
    def validation_errors(request, exc):
        error_response = ErrorType.INVALID_ARGUMENT.create_error_response(str(exc))
        return api.create_response(
            request,
            error_response,
            status=422,
        )

    # django ninja 내장 AuthenticationError 핸들러 override
    @api.exception_handler(AuthenticationError)
    def authentication_errors(request, exc):
        error_response = ErrorType.UNAUTHENTICATED.create_error_response(str(exc))
        return api.create_response(
            request,
            error_response,
            status=401,
        )

    # django ninja 내장 Http404 핸들러 override
    @api.exception_handler(Http404)
    def http404_errors(request, exc):
        error_response = ErrorType.NOT_FOUND.create_error_response(str(exc))
        return api.create_response(
            request,
            error_response,
            status=404,
        )

    #
    # 커스텀 추가 에러 핸들러
    #

    # 권한 에러 핸들러
    @api.exception_handler(PermissionError)
    def permission_errors(request, exc):
        error_response = ErrorType.PERMISSION_DENIED.create_error_response(str(exc))
        return api.create_response(
            request,
            error_response,
            status=403,
        )