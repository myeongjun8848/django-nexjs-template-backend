from enum import Enum
from dataclasses import dataclass
from http import HTTPStatus

@dataclass(frozen=True)
class ErrorDetail:
    status_code: int
    error_code: int
    message: str

class ErrorCategory:
    CLIENT = 4000  # 클라이언트 에러는 4000대
    SERVER = 5000  # 서버 에러는 5000대
    SECURITY = 6000  # 보안 관련 에러는 6000대

class ErrorType(Enum):
    CANCELLED = ErrorDetail(
        status_code=HTTPStatus.BAD_REQUEST,
        error_code=ErrorCategory.CLIENT + 1,
        message="The operation was cancelled"
    )
    INVALID_ARGUMENT = ErrorDetail(
        status_code=HTTPStatus.BAD_REQUEST,
        error_code=ErrorCategory.CLIENT + 2,
        message="Invalid argument"
    )
    NOT_FOUND = ErrorDetail(
        status_code=HTTPStatus.NOT_FOUND,
        error_code=ErrorCategory.CLIENT + 3,
        message="Resource not found"
    )
    ALREADY_EXISTS = ErrorDetail(
        status_code=HTTPStatus.CONFLICT,
        error_code=ErrorCategory.CLIENT + 4,
        message="Resource already exists"
    )
    RESOURCE_EXHAUSTED = ErrorDetail(
        status_code=HTTPStatus.TOO_MANY_REQUESTS,
        error_code=ErrorCategory.CLIENT + 5,
        message="Resource exhausted"
    )
    FAILED_PRECONDITION = ErrorDetail(
        status_code=HTTPStatus.BAD_REQUEST,
        error_code=ErrorCategory.CLIENT + 6,
        message="Operation was rejected because the system is not in a state required for the operation's execution"
    )
    ABORTED = ErrorDetail(
        status_code=HTTPStatus.CONFLICT,
        error_code=ErrorCategory.CLIENT + 7,
        message="The operation was aborted, typically due to a concurrency issue such as a sequencer check failure"
    )
    OUT_OF_RANGE = ErrorDetail(
        status_code=HTTPStatus.BAD_REQUEST,
        error_code=ErrorCategory.CLIENT + 8,
        message="Operation was attempted past the valid range"
    )
    UNKNOWN = ErrorDetail(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        error_code=ErrorCategory.SERVER + 1,
        message="Unknown error"
    )
    DEADLINE_EXCEEDED = ErrorDetail(
        status_code=HTTPStatus.GATEWAY_TIMEOUT,
        error_code=ErrorCategory.SERVER + 2,
        message="Deadline expired before operation could complete"
    )
    UNIMPLEMENTED = ErrorDetail(
        status_code=HTTPStatus.NOT_IMPLEMENTED,
        error_code=ErrorCategory.SERVER + 3,
        message="Operation is not implemented or not supported/enabled in this service"
    )
    INTERNAL = ErrorDetail(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        error_code=ErrorCategory.SERVER + 4,
        message="Internal error encountered"
    )
    UNAVAILABLE = ErrorDetail(
        status_code=HTTPStatus.SERVICE_UNAVAILABLE,
        error_code=ErrorCategory.SERVER + 5,
        message="The service is currently unavailable"
    )
    DATA_LOSS = ErrorDetail(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        error_code=ErrorCategory.SERVER + 6,
        message="Unrecoverable data loss or corruption"
    )
    PERMISSION_DENIED = ErrorDetail(
        status_code=HTTPStatus.FORBIDDEN,
        error_code=ErrorCategory.SECURITY + 2,
        message="Permission denied"
    )
    UNAUTHENTICATED = ErrorDetail(
        status_code=HTTPStatus.UNAUTHORIZED,
        error_code=ErrorCategory.SECURITY + 1,
        message="Unauthenticated"
    )
    