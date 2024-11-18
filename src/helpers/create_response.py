from typing import Any, Dict, Optional
from helpers.error.types import ErrorType


def create_success_response(data: Any) -> Dict[str, Any]:
    return {
        "status": "success",
        "data": data,
        "error": None
    }

def create_error_response(error_type: ErrorType, message: Optional[str] = None) -> dict:
    return {
        "status": "error",
        "data": None,
        "error": {
            "error_code": error_type.value.error_code,
            "message": message if message is not None else error_type.value.message,
        }
    }