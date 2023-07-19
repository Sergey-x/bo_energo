import math

import fastapi as fa
from fastapi.responses import ORJSONResponse
from schemas.task_1 import GetDiscriminantResponseSchema


api_router = fa.APIRouter()


@api_router.get(
    "/",
    response_class=ORJSONResponse,
    response_model=GetDiscriminantResponseSchema,
    status_code=fa.status.HTTP_200_OK,
    responses={
        fa.status.HTTP_200_OK: {
            "description": "Ok",
        },
        fa.status.HTTP_401_UNAUTHORIZED: {
            "description": "Could not validate credentials",
        },
        fa.status.HTTP_404_NOT_FOUND: {
            "description": "Not found",
        },
    },
)
async def get_post_by_id(
        a: float = fa.Query(),
        b: float = fa.Query(),
        c: float = fa.Query(),
):
    """"""
    discriminant: float = (b * b) - (4 * a * c)

    if discriminant < 0:
        return GetDiscriminantResponseSchema(x1=None, x2=None)
    if discriminant == 0:
        x: float = -b / (2 * a)
        return GetDiscriminantResponseSchema(x1=x, x2=x)
    else:
        x1: float = (-b + math.sqrt(discriminant)) / (2 * a)
        x2: float = (-b - math.sqrt(discriminant)) / (2 * a)
        return GetDiscriminantResponseSchema(x1=x1, x2=x2)
