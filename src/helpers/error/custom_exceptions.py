from typing import Optional
from .types import ErrorType

class CustomAPIException(Exception):
    def __init__(
        self, 
        error_type: ErrorType,
        detail: Optional[str] = None
    ):
        super().__init__(detail or error_type.message)
        self.error_type = error_type
        self.detail = detail
        
    @property
    def error_detail(self) -> dict:
        return {
            "code": self.error_type.error_code,
            "message": self.detail or self.error_type.message
        }

