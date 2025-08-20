from typing import Any, Dict
from fastapi import HTTPException, status

class APIError(HTTPException):
    def __init__(self, status_code: int,
                 detail: Any = None,
                 ) -> None:
        super().__init__(status_code, detail)

class UnauthorizedError(APIError):
    def __init__(self, status_code: int = status.HTTP_401_UNAUTHORIZED, 
                 detail: str = "Not authinticated"): 
        super().__init__(status_code, detail)

class EmailNotExistError(APIError):
    def __init__(self, status_code: int = status.HTTP_401_UNAUTHORIZED ,
                  detail: str = "Email not exist"):
        super().__init__(status_code, detail)

class EmailExistError(APIError):
    def __init__(self, status_code: int = status.HTTP_400_BAD_REQUEST ,
                  detail: str = "Email exist"):
        super().__init__(status_code, detail)

class InvalidPasswordError(APIError):
    def __init__(self, status_code: int = status.HTTP_401_UNAUTHORIZED, 
                 detail: str = "Invalid password") -> None:
        super().__init__(status_code, detail)


class InvalidTokenError(APIError):
    def __init__(self, status_code: int = status.HTTP_401_UNAUTHORIZED, 
                 detail: str = "invalid access token"):
        super().__init__(status_code, detail)

class BadProductListError(APIError):
    def __init__(self, status_code: int = status.HTTP_400_BAD_REQUEST, detail: str = "Bad Product list") -> None:
        super().__init__(status_code, detail)