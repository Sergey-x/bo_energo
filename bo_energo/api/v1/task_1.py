import fastapi as fa
from fastapi.responses import ORJSONResponse
from schemas.task_1 import GetEquationSolutionRequestSchema, GetEquationSolutionResponseSchema
from services.equation import get_equation_roots


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
    x1, x2 = get_equation_roots(a=args.a, b=args.b, c=args.c)
    return GetEquationSolutionResponseSchema(x1=x1, x2=x2)
