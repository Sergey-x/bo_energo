import fastapi as fa

from .v1 import task_1_router


api_router = fa.APIRouter()

api_router.include_router(task_1_router, prefix="/task1", tags=["task1"])
