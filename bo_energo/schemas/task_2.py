import pydantic as pd
from enums.color import ColorEnum


MIN_NUMBER: int = 1
MAX_NUMBER: int = 100


class GetColorRequestSchema(pd.BaseModel):
    number: pd.conint(ge=MIN_NUMBER, le=MAX_NUMBER)


class GetColorResponseSchema(pd.BaseModel):
    color: ColorEnum
