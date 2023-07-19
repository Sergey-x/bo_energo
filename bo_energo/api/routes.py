import fastapi as fa

from .v1 import task_1_router, task_2_router


api_router = fa.APIRouter()

api_router.include_router(task_1_router, prefix="/roots", tags=["tasks"])
api_router.include_router(task_2_router, prefix="/color", tags=["tasks"])
