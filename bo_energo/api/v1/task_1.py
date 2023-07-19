import math

import fastapi as fa
from fastapi.responses import ORJSONResponse
from schemas.task_1 import GetEquationSolutionRequestSchema, GetEquationSolutionResponseSchema


api_router = fa.APIRouter()


@api_router.get(
    "/",
    response_class=ORJSONResponse,
    response_model=GetEquationSolutionResponseSchema,
    status_code=fa.status.HTTP_200_OK,
    responses={
        fa.status.HTTP_200_OK: {
            "description": "Ok",
        },
        fa.status.HTTP_400_BAD_REQUEST: {
            "description": "Некорректный формат входных данных.",
        },
    },
)
async def get_solution(
        args: GetEquationSolutionRequestSchema = fa.Depends(),
):
    """Получить корни квадратного уравнения.

    Если корней нет, оба поля в ответе равны None.
    Если корень один, оба поля в ответе равны этому корню.
    """
    a: float = args.a
    b: float = args.b
    c: float = args.c

    discriminant: float = (b * b) - (4 * a * c)

    if discriminant < 0:
        return GetEquationSolutionResponseSchema(x1=None, x2=None)
    if discriminant == 0:
        x: float = -b / (2 * a)
        return GetEquationSolutionResponseSchema(x1=x, x2=x)
    if discriminant > 0:
        x1: float = (-b + math.sqrt(discriminant)) / (2 * a)
        x2: float = (-b - math.sqrt(discriminant)) / (2 * a)
        return GetEquationSolutionResponseSchema(x1=x1, x2=x2)
