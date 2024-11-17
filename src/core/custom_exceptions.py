from typing import Any, Dict, Tuple

class CustomAPIException(Exception):
    def __init__(
        self, 
        error_type: Tuple[int, Dict[str, Any]],
        detail: str = None
    ):
        super().__init__(detail or error_type[1]["message"])
        self.status_code = error_type[0]
        self.error_code = error_type[1]["code"]
        self.message = detail or error_type[1]["message"]
        
    @property
    def error_detail(self) -> Dict[str, Any]:
        return {
            "code": self.error_code,
            "message": self.message
        }
