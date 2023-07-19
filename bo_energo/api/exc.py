import fastapi as fa
from fastapi.responses import ORJSONResponse


def validation_exception_handler(request: fa.Request, exc):
    """Exception handler for pydantic validation errors"""
    return ORJSONResponse(
        status_code=fa.status.HTTP_400_BAD_REQUEST,
        content={"detail": "Bad request"}
    )
