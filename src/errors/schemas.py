from ninja import Schema
from typing import Optional

class ErrorDetail(Schema):
    code: int
    message: str
    detail: Optional[str] = None
    status: str

class ErrorOut(Schema):
    error: ErrorDetail