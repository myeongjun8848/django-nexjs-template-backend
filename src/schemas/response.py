from typing import Generic, TypeVar
from ninja import Schema

T = TypeVar('T')

class SuccessResponse(Schema, Generic[T]):
    status: str = "success"
    data: T
    error: None = None

class ErrorDetail(Schema):
    error_code: int
    message: str

class ErrorResponse(Schema):
    status: str = "error"
    data: None = None
    error: ErrorDetail
