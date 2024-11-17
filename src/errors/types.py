from enum import Enum
from typing import Dict, Any

class ErrorType(Enum):
    CANCELLED = (499, {"code": 1, "message": "The operation was cancelled, typically by the caller."})
    UNKNOWN = (500, {"code": 2, "message": "Unknown error."})
    INVALID_ARGUMENT = (400, {"code": 3, "message": "Invalid argument."})
    DEADLINE_EXCEEDED = (504, {"code": 4, "message": "Deadline expired before operation could complete."})
    NOT_FOUND = (404, {"code": 5, "message": "Resource not found."})
    ALREADY_EXISTS = (409, {"code": 6, "message": "Resource already exists."})
    PERMISSION_DENIED = (403, {"code": 7, "message": "Permission denied."})
    UNAUTHENTICATED = (401, {"code": 16, "message": "Unauthenticated."})
    RESOURCE_EXHAUSTED = (429, {"code": 8, "message": "Resource exhausted."})
    FAILED_PRECONDITION = (400, {"code": 9, "message": "Operation was rejected because the system is not in a state required for the operation's execution."})
    ABORTED = (409, {"code": 10, "message": "The operation was aborted, typically due to a concurrency issue such as a sequencer check failure."})
    OUT_OF_RANGE = (400, {"code": 11, "message": "Operation was attempted past the valid range."})
    UNIMPLEMENTED = (501, {"code": 12, "message": "Operation is not implemented or not supported/enabled in this service."})
    INTERNAL = (500, {"code": 13, "message": "Internal error encountered."})
    UNAVAILABLE = (503, {"code": 14, "message": "The service is currently unavailable."})
    DATA_LOSS = (500, {"code": 15, "message": "Unrecoverable data loss or corruption."})

    def __init__(self, status_code: int, error_info: Dict):
        self.status_code = status_code
        self.error_info = error_info

    def create_error_response(self, detail: str = None) -> Dict[str, Any]:
        return {
            "error": {
                "code": self.status_code,
                "message": self.error_info["message"],
                "detail": detail,
                "status": self.name
            }
        }
