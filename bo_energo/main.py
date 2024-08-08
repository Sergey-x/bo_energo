import fastapi as fa
from api import api_router
from api.exc import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from pydantic_core import ValidationError


def get_app() -> fa.FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "Тестовое."

    application = fa.FastAPI(
        title="БО-ЭНЕРГО",
        description=description,
        version="0.1.0",
    )

    # подключение api handlers
    application.include_router(api_router)

    application.add_exception_handler(RequestValidationError, validation_exception_handler)
    application.add_exception_handler(ValidationError, validation_exception_handler)

    return application


app = get_app()
