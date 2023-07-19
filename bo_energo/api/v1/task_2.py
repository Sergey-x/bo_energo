import fastapi as fa
from enums.color import ColorEnum
from fastapi.responses import ORJSONResponse
from schemas.task_2 import GetColorRequestSchema, GetColorResponseSchema


api_router = fa.APIRouter()


@api_router.get(
    "/",
    response_class=ORJSONResponse,
    response_model=GetColorResponseSchema,
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
async def get_color(
        _: GetColorRequestSchema = fa.Depends(),
):
    """
    Предположим, что предметов зеленого цвета равно x.
    Тогда предметов синего цвета равно 10x (сильно больше ~ где-то на порядок).
    Предметов красного цвета равно x - 5 (чуть меньше - где-то на 5%).

    Всего: x + 10x + x - 5 = 100  (x ~ 8).
    Вероятность около 80% (для синего) является приемлемой в заданных условиях,
    поэтому для простоты всегда возвращаем его.
    """
    return GetColorResponseSchema(color=ColorEnum.BLUE)
